from dotenv import load_dotenv
load_dotenv()
import os

class Comms:
    # User facing properties:
    #   None

    def __init__(self, client):
        self.client = client

    def send_text_message(self, phone_number, message):
        # Parameters:
        #   phone_number: string value
        #   message: string value
        # Side effects: 
        #   sends text message
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN') 
        account_sid = "AC6d9c86f8b137031e76010c39428f8b8d"
        client = self.client(account_sid, auth_token)
        client.messages.create(
        to=f"+44{int(phone_number)}", 
        from_="++447897026700",
        body= message)

        
