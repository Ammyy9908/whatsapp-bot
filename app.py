from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route('/')
def index():
    return 'Phirlo Whatsapp Bot'


@app.route('/sms', methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    resp = MessagingResponse()
    if msg == 'start':
        resp.message("Hello,Welcome to Phirlo Ltd. We are here to help you with your queries. Please select an option from the menu below.")
        resp.message("1. Register")
        resp.message("2. Declutter your old clothes")
        
    

    # # Create reply
    
    resp.message("You said: {}".format(msg))

    return str(resp)


if __name__=="__main__":
  app.run()
