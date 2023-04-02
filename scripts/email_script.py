import requests


def main():
    body = """<html>
              <head></head>
              <body>
                <p>Test Email!<br>
                   How are you? <br>
                   <img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2013%2F10%2F09%2F02%2F27%2Flake-192990__340.jpg&tbnid=Em8YFndBfKYAnM&vet=12ahUKEwjw8vCDtoj-AhWk5HMBHVmqDYEQMygQegUIARDYAQ..i&imgrefurl=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fhouse%2F&docid=hhUynytURgfY2M&w=510&h=340&q=image&ved=2ahUKEwjw8vCDtoj-AhWk5HMBHVmqDYEQMygQegUIARDYAQ">
                </p>
              </body>
            </html>
        """
    subject = "How are you doing?"
    data = {
        "body": body,
        "subject": subject
    }
    response = requests.post('http://localhost:5000/mail/send/', data=data)
    print(response.text)

main()
