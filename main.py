import datetime as dt
from flask import Flask
from flask import request
from flask import render_template


MIN_NAME_LENGTH = 3
MAX_NAME_LENGTH = 100

MIN_MESSAGE_LENGTH = 1
MAX_MESSAGE_LENGTH = 3000

all_messages = []

application = Flask(__name__)


@application.route("/chat")
def display_chat():
    return render_template("form.html")


@application.route("/")
def index_page():
    return "Hello, welcome to Skillbox chat"


@application.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@application.route("/send_message", methods=["POST", "GET"])
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    if len(sender) > MAX_NAME_LENGTH or len(sender) < MIN_NAME_LENGTH:
        sender = "ERROR"
        text = f"Имя должно быть длинее чем {MIN_NAME_LENGTH} и короче чем {MAX_NAME_LENGTH} символов"
    if len(text) < MIN_MESSAGE_LENGTH or len(text) > MAX_MESSAGE_LENGTH:
        sender = "ERROR"
        text = f"Сообщение должно быть длинее чем {MIN_MESSAGE_LENGTH} и короче чем {MAX_MESSAGE_LENGTH} символов"
    add_message(sender, text)



def print_message(mess):
    print(f"[{mess['sender']}]: {mess['text']} / {mess['time']}")


def add_message(sender, text):
    # 1. Подготовить словарь с данными сообщения
    new_message = {
        "sender": sender,
        "text": text,
        "time": dt.datetime.now().strftime('%H:%M:%S'),
    }
    all_messages.append(new_message)


# add_message("Митя", "Всем привет")
#
# for message in all_messages:
#     print_message(message)

application.run()
