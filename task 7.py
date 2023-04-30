import vk_api


TOKEN = "vk1.a.e3UiV626Dz0XlG06ET2URvC0uEb0I2362oJoAMe1Z1L-nm3ZSlOIMfaKRIQxPF9eBwjwWFYKAXNAUZJYzMNctgLX8bFfftXUZEC_9t7WdOO0LtyZBCUdXaFu8pEZg95ALbIPCyvrKBOkHUhr9f8gMjBFa6Mscn5zoAQ_BA7qY9goPZEvS4jTKeg6LBY7XEhpzxQMRudB4V1Gi4PRP-FxrQ"


def main():
    login, password = LOGIN, PASSWORD
    vk_sess = vk_api.VkApi(login, password)

    try:
        vk_sess.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vkAPI = vk_sess.get_api()
    group_id = -220218364
    album_id = 291217166
    photos = vkAPI.photos.get(owner_id=group_id, album_id=album_id)

    for photo in photos["items"]:
        print(f"Link: {photo['sizes'][-1]['url']}")
        print(f"Size: {photo['sizes'][-1]['width']}x{photo['sizes'][-1]['height']}")


if __name__ == '__main__':
    main()