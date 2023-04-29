import vk_api
from datetime import datetime


def main():
    login, password = "+79819718551", "Maksx006"
    vk_sess = vk_api.VkApi(login, password)
    try:
        vk_sess.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vkAPI = vk_sess.get_api()

    response = vkAPI.wall.get(count=5, offset=0)
    if response['items']:
        for post_num, current_post in enumerate(response['items']):
            print(f"text: {current_post['text']}")
            print(f"date: {datetime.utcfromtimestamp(current_post['date']).strftime('%Y-%m-%d')}")
            print(f"time: {datetime.utcfromtimestamp(current_post['date']).strftime('%H:%M:%S')}")
            print()


if __name__ == '__main__':
    main()