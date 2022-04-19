import datetime as dt


def print_message(mess):
    print(f"[{mess['sender']}]: {mess['text']} / {mess['time']}")

def add_message(sender, text):
    # 1. Подготовить словарь с данными сообщения
    new_message = {
        "sender": sender,
        "text": text,
        "time": dt.datetime.now().strftime('%H:%M')
    }
    all_messages.append(new_message)

message1 = {
    'sender': "Яг Янов",
    'text': "А конфеты вы тоже за меня будете есть?",
    'time': '22:55'
}
message2 = {
    'sender': "Еще кто-то?",
    'text': "Что делать?",
    'time': '22:55'
}

all_messages = [message1, message2]

add_message("Митя", "Всем привет")

for message in all_messages:
    print_message(message)