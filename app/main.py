from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return 'Phirlo Whatsapp Bot'


@app.route('/sms', methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body').lower()
    resp = MessagingResponse()
    if msg == 'hi':
        resp.message("Hello,How can i help you?")
    if 'quote' in msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        resp.mesaage(quote)
            

    return str(resp)




# incoming_msg = request.values.get('Body', '').lower()
    
#     msg = resp.message()
#     responded = False
#     if 'quote' in incoming_msg:
#         # return a quote
#         r = requests.get('https://api.quotable.io/random')
#         if r.status_code == 200:
#             data = r.json()
#             quote = f'{data["content"]} ({data["author"]})'
#         else:
#             quote = 'I could not retrieve a quote at this time, sorry.'
#         msg.body(quote)
#         responded = True
#     if 'cat' in incoming_msg:
#         # return a cat pic
#         msg.media('https://cataas.com/cat')
#         responded = True
#     if not responded:
#         msg.body('I only know about famous quotes and cats, sorry!')
#     return str(resp)
