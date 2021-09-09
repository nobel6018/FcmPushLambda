import unittest

from main import entrypoint


class TestFirebaseIntegration(unittest.TestCase):

    def test_send_one_data(self):
        # given
        event = {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': None,
                 'data': 'eyJwdXNoVHlwZSI6IlNJTkdMRV9NRVNTQUdFIiwiZGV2aWNlVG9rZW4iOiJlZkVMU1FBTlNrS21WUVZLMF81M1NqOkFQQTkxYkZkdVI1T1FHWWRfUW83MEowUDZkUnNMN2k5a0hBR2p3Y1FObGRxR1hQU1RjRkhvRm9kY01RZTVXRjZ0MW5MUnNKRGc2bjZnWmEtNWg2ZW5TSmoyWlZkN1Zsb1cxRFBkSEFzV000d2hyZGl6bk9OUEYyQUVJUGU0SkNOVElqY3lRcnlkRVkzIiwidGl0bGUiOiJ0aXRsZSBmcm9tIGFwaSIsImJvZHkiOiJib2R5IGZyb20gYXBpIiwiZGF0YSI6eyJjbGlja1VybCI6InBvaW50YmVycnk6Ly9hdHRlbmRhbmNlIn19'}

        # when
        result = entrypoint(event, None)

        # then
        self.assertTrue(result.startswith("successfully Sent message: projects/pointberry-292606/messages/"))

    def test_send_one_null_data_field(self):
        # given
        event = {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': None,
                 'data': 'eyJwdXNoVHlwZSI6IlNJTkdMRV9NRVNTQUdFIiwiZGV2aWNlVG9rZW4iOiJlZkVMU1FBTlNrS21WUVZLMF81M1NqOkFQQTkxYkZkdVI1T1FHWWRfUW83MEowUDZkUnNMN2k5a0hBR2p3Y1FObGRxR1hQU1RjRkhvRm9kY01RZTVXRjZ0MW5MUnNKRGc2bjZnWmEtNWg2ZW5TSmoyWlZkN1Zsb1cxRFBkSEFzV000d2hyZGl6bk9OUEYyQUVJUGU0SkNOVElqY3lRcnlkRVkzIiwidGl0bGUiOiJ0aXRsZSBmcm9tIGFwaSIsImJvZHkiOiJtZXNzYWdlIGZyb20gYXBpIiwiZGF0YSI6bnVsbH0='}

        # when
        result = entrypoint(event, None)

        # then
        self.assertTrue(result.startswith("successfully Sent message: projects/pointberry-292606/messages/"))

    def test_no_such_device_token(self):
        # given
        event = {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': None,
                 'data': 'eyJwdXNoVHlwZSI6IlNJTkdMRV9NRVNTQUdFIiwiZGV2aWNlVG9rZW4iOiJmcGpnT0RvaVRuS2J3UkpDYkhoYkU1OkFQQTkxYkU2VkZoZW9xdC1ZTEFWR0syY0NCX0VOWl9WOVQ3RXRfa2hrMHRMRUMySDhhUkFMYnh2S2ZZZTY0MmJ6eFN1dVZRc0lvTFZKa3ltMVpJQ2wwR21LdDhXYlV0aFFBMDZ4MFQwOWtGTFRvYm9rTTZvWjlQbTRTMW9VbHJFTDlSMkhKamlOMlUyIiwidGl0bGUiOiJ0aXRsZSBmcm9tIGFwaSIsImJvZHkiOiJib2R5IGZyb20gYXBpIiwiZGF0YSI6eyJjbGlja1VybCI6InBvaW50YmVycnk6Ly9hdHRlbmRhbmNlIn19'}

        # when
        result = entrypoint(event, None)

        # then
        self.assertEqual(
            "No such deviceToken: fpjgODoiTnKbwRJCbHhbE5:APA91bE6VFheoqt-YLAVGK2cCB_ENZ_V9T7Et_khk0tLEC2H8aRALbxvKfYe642bzxSuuVQsIoLVJkym1ZICl0GmKt8WbUthQA06x0T09kFLTobokM6oZ9Pm4S1oUlrEL9R2HJjiN2U2",
            result
        )

    def test_invalid_FCM_registration_token(self):
        # given
        event = {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': None,
                 'data': 'eyJwdXNoVHlwZSI6IlNJTkdMRV9NRVNTQUdFIiwiZGV2aWNlVG9rZW4iOiJlZkVMU1FBTlNrS21WUVZLMF81M1NqOkFQQTkxYkZkdVI1T1FHWWRfUW83MEowUDZkUnNMN2k5a0hBR2p3Y1FObGRxR1hQU1RjRkhvRm9kY01RZTVXRjZ0MW5MUnNKRGc2bjZnWmEtNWg2ZW5TSmoyWlZkN1Zsb1cxRFBkSEFzV000d2hyZGl6bk9OUEYyQUVJUGU0SkNOVElqY3lRcnlkenp6IiwidGl0bGUiOiJ0aXRsZSBmcm9tIGFwaSIsImJvZHkiOiJib2R5IGZyb20gYXBpIiwiZGF0YSI6eyJjbGlja1VybCI6InBvaW50YmVycnk6Ly9hdHRlbmRhbmNlIn19'}

        # when
        result = entrypoint(event, None)

        # then
        self.assertEqual(
            "The registration token is not a valid FCM registration token: $efELSQANSkKmVQVK0_53Sj:APA91bFduR5OQGYd_Qo70J0P6dRsL7i9kHAGjwcQNldqGXPSTcFHoFodcMQe5WF6t1nLRsJDg6n6gZa-5h6enSJj2ZVd7VloW1DPdHAsWM4whrdiznONPF2AEIPe4JCNTIjcyQrydzzz",
            result
        )


if __name__ == '__main__':
    unittest.main()
