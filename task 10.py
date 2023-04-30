import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime


GROUP_ID = 220218364
TOKEN = "vk1.a.e3UiV626Dz0XlG06ET2URvC0uEb0I2362oJoAMe1Z1L-nm3ZSlOIMfaKRIQxPF9eBwjwWFYKAXNAUZJYzMNctgLX8bFfftXUZEC_9t7WdOO0LtyZBCUdXaFu8pEZg95ALbIPCyvrKBOkHUhr9f8gMjBFa6Mscn5zoAQ_BA7qY9goPZEvS4jTKeg6LBY7XEhpzxQMRudB4V1Gi4PRP-FxrQ"
login, password = LOGIN, PASSWORD
DAYS_OF_WEEK = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


def main():
    first_message = True
    vk_sess = vk_api.VkApi(token=TOKEN)
    long_poll = VkBotLongPoll(vk_sess, GROUP_ID)
    vkAPI = vk_sess.get_api()

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message = "Hello, you can write the date in the format \"YYYY-MM-DD\" and I will say the day of week"

            if first_message:
                vkAPI.messages.send(user_id=event.obj.message['from_id'],
                                    message=message,
                                    random_id=random.randint(0, 2 ** 64))
                first_message = False
            else:
                week_day = DAYS_OF_WEEK[datetime.date(*map(int, event.obj.message["text"].split("-"))).weekday()]

                vkAPI.messages.send(user_id=event.obj.message["from_id"],
                                    message=f"День недели - {week_day}",
                                    random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()