# -*- coding: utf-8 -*-
# Import libraries
from twilio.rest import Client
from flask import Flask, request
from twilio import twiml
import config
import google_drive

def textMe(messageBody):
    # Your Account SID from twilio.com/console
    account_sid = config.account_sid
    # Your Auth Token from twilio.com/console
    auth_token  = config.auth_token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=config.to,
        from_=config.from_,
        body=messageBody)

    print(message.sid)



def main():
    # Define variable for message_body
    receivedMessage = "Hello"

    # textMe("Hello Zach. How are you?")
    app = Flask(__name__)
    @app.route('/sms', methods=['POST'])
    def sms():
        variableName = u'Budget'
        variableName2 = u'Full budget'
        number = request.form['From']
        message_body = request.form['Body']
        receivedMessage = message_body
        if message_body.encode('utf8') == variableName.encode('utf8'):
            textBody = google_drive.beautifulBudget()
            textMe(textBody)
        elif message_body.encode('utf8') == variableName2.encode('utf8'):
            textBody = google_drive.getFullSum()
            textMe(textBody)
        else:
            textMe("I'm too stupid to understand that")
        return message_body

    app.run()

    print(receivedMessage)


if __name__ == "__main__":
	main()
