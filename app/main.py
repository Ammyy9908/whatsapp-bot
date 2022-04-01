from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>I want to Deploy Flask to Heroku</h1>'


@app.route('/sms', methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    resp = MessagingResponse()
    msg = request.form.get('Body')
    if msg == 'hi':
        
        resp.message("Hello,How can i help you?")

    # Create reply
    
    resp.message("You said: {}".format(msg))

    return str(resp)
