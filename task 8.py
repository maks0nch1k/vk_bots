import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


GROUP_ID = 220218364
ALBUM_ID = 291217166
TOKEN = "vk1.a.e3UiV626Dz0XlG06ET2URvC0uEb0I2362oJoAMe1Z1L-nm3ZSlOIMfaKRIQxPF9eBwjwWFYKAXNAUZJYzMNctgLX8bFfftXUZEC_9t7WdOO0LtyZBCUdXaFu8pEZg95ALbIPCyvrKBOkHUhr9f8gMjBFa6Mscn5zoAQ_BA7qY9goPZEvS4jTKeg6LBY7XEhpzxQMRudB4V1Gi4PRP-FxrQ"
login, password = LOGIN, PASSWORD


def get_random_photo_id():
    vk_sess = vk_api.VkApi(login, password)

    try:
        vk_sess.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vkAPI = vk_sess.get_api()
    photos = vkAPI.photos.get(owner_id=-GROUP_ID, album_id=ALBUM_ID)
    photo = random.choice(photos["items"])

    return f"photo{photo['owner_id']}_{photo['id']}"


def main():
    vk_sess = vk_api.VkApi(token=TOKEN)
    vkPI = vk_sess.get_api()

    long_poll = VkBotLongPoll(vk_sess, GROUP_ID)

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj.message["from_id"]
            user = vkPI.users.get(user_id=user_id)
            random_photo_id = get_random_photo_id()

            vkPI.messages.send(user_id=user_id,
                               message=f"Hello, {user[0]['first_name']}",
                               random_id=random.randint(0, 2 ** 64),
                               attachment=random_photo_id)


if __name__ == '__main__':
    main()