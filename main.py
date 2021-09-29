import base64
import json
import logging
from enum import Enum
from typing import Optional

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging


# https://cloud.google.com/functions/docs/calling/pubsub
def entrypoint(event: dict, context) -> str:
    FIREBASE_ACCOUNT_SERVICE = "./sample-project-5d15z-firebase-adminsdk-gabge-4fa79ee667.json"
    try:
        cred = credentials.Certificate(FIREBASE_ACCOUNT_SERVICE)
        firebase_admin.initialize_app(cred)
    except ValueError:  # The default Firebase app already exists. This means you called initialize_app() more than once
        pass

    logging.info("event: ", event)
    print("event:", event)
    data = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    push_type: str = data['pushType']
    if push_type != PushType.SINGLE_MESSAGE.name:
        print("Not supported message type", push_type)

    device_token = data['deviceToken']
    title: str = data['title']
    body: str = data['body']
    metadata: dict = data.get('data', None)

    return send_one_data(device_token, title, body, metadata)


def send_one_data(device_token: str, title: str, body: str, data: Optional[dict]) -> str:
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        data=data,
        token=device_token,
    )

    try:
        response = messaging.send(message)
        print("successfully Sent message:", response)
        return f"successfully Sent message: {response}"
    except firebase_admin._messaging_utils.UnregisteredError:
        print(f"No such deviceToken: {device_token}")
        return f"No such deviceToken: {device_token}"
    except firebase_admin.exceptions.InvalidArgumentError:
        return f"The registration token is not a valid FCM registration token: ${device_token}"


class PushType(Enum):
    SINGLE_MESSAGE = 1
    MULTIPLE_MESSAGE = 2
