import requests
import json

def main():
    body = """<html>
              <head></head>
              <body>
                <p>Test Email!<br>
                   How are you? <br>
                   <img src="http://35.240.237.249:5000/mail/tracker?id={id}">
                </p>
              </body>
            </html>
        """
    subject = "How are you doing?"
    data = {
        "body": body,
        "subject": subject
    }
    response = requests.post('http://35.240.237.249:5000/api/mail/send', data=json.dumps(data))
    print(response.text)

main()