import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

TOKEN = "vk1.a.e3UiV626Dz0XlG06ET2URvC0uEb0I2362oJoAMe1Z1L-nm3ZSlOIMfaKRIQxPF9eBwjwWFYKAXNAUZJYzMNctgLX8bFfftXUZEC_9t7WdOO0LtyZBCUdXaFu8pEZg95ALbIPCyvrKBOkHUhr9f8gMjBFa6Mscn5zoAQ_BA7qY9goPZEvS4jTKeg6LBY7XEhpzxQMRudB4V1Gi4PRP-FxrQ"


def main():
    vk_sess = vk_api.VkApi(token=TOKEN)
    long_poll = VkBotLongPoll(vk_sess, 220218364)

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj.message['from_id']
            vkAPI = vk_sess.get_api()
            user = vkAPI.users.get(user_id=user_id, fields="city")[0]
            message = f"Привет, {user['first_name']}!"
            if "city" in user:
                message += f" Как поживает {user['city']['title']}?"
            vkAPI.messages.send(user_id=user_id,
                                message=message,
                                random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()