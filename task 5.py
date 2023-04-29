import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import datetime
import random

TOKEN = "vk1.a.e3UiV626Dz0XlG06ET2URvC0uEb0I2362oJoAMe1Z1L-nm3ZSlOIMfaKRIQxPF9eBwjwWFYKAXNAUZJYzMNctgLX8bFfftXUZEC_9t7WdOO0LtyZBCUdXaFu8pEZg95ALbIPCyvrKBOkHUhr9f8gMjBFa6Mscn5zoAQ_BA7qY9goPZEvS4jTKeg6LBY7XEhpzxQMRudB4V1Gi4PRP-FxrQ"
WEEK_DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


def main():
    vk_sess = vk_api.VkApi(token=TOKEN)

    long_poll = VkBotLongPoll(vk_sess, 220218364)

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message_text = event.obj.message['text']
            if "время" in message_text.lower() or "число" in message_text.lower() or \
                    "дата" in message_text.lower() or "день" in message_text.lower():
                answer = f"Сейчас {datetime.datetime.now()}, {WEEK_DAYS[datetime.datetime.now().weekday()]}"
            else:
                answer = "Вы можете спросить меня о времени!"

            vkAPI = vk_sess.get_api()
            vkAPI.messages.send(user_id=event.obj.message['from_id'],
                                message=answer,
                                random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()