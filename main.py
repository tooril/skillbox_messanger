import datetime as dt
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import abort

MIN_NAME_LENGTH = 10
MAX_NAME_LENGTH = 100

MIN_MESSAGE_LENGTH = 10
MAX_MESSAGE_LENGTH = 3000

all_messages = []

application = Flask(__name__)


@application.route("/chat")
def display_chat():
    return render_template("form.html")

@application.route("/error_mess")
def error_mess():
    return render_template("error_mess.html")


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
    # if MIN_NAME_LENGTH <= len(sender) <= MAX_NAME_LENGTH or\
    #     MIN_MESSAGE_LENGTH <= len(text) <= MAX_MESSAGE_LENGTH:
    #     add_message(sender, text)
    #     return "Сообщение принято"
    # else:
    #return render_template("error_mess.html")#redirect(url_for("error_mess"))


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
