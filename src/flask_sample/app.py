from time import sleep

from flask import Flask

app = Flask(__name__)


def write_notification(filename: str, email: str, message=""):
    with open(filename, mode="a") as email_file:
        for i in range(10):
            content = f"{i}: notification for {email}: {message}"
            print(content)
            email_file.write(f"{content}\n")
            sleep(1)


@app.route("/")
def hello():
    email = "test2@test.com"
    write_notification("log_1.txt", email, message="await notification"),
    write_notification("log_2.txt", email, message="await2 notification")
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)