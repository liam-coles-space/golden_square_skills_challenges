from lib.comms import *
from unittest.mock import Mock

def test_construct_comms():
    twilio_mock = Mock()
    comms = Comms(twilio_mock)
    assert comms.client == twilio_mock

"""
When send_text_message is called with phone_number and message
twilio helper method create should be called with phone_number and message
"""
def test_send_text_message_calls_twilio_correctly():
    twilio_mock = Mock()
    client_mock = Mock()
    messages_mock = Mock()
    twilio_mock.return_value = client_mock
    client_mock.messages = messages_mock
    comms = Comms(twilio_mock)
    comms.send_text_message('01733567124', 'I am a message')
    messages_mock.create.assert_called_with(to='+441733567124', from_='++447897026700', body='I am a message')
    
