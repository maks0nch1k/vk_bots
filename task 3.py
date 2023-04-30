import vk_api
import os


TOKEN = "vk1.a.e3UiV626Dz0XlG06ET2URvC0uEb0I2362oJoAMe1Z1L-nm3ZSlOIMfaKRIQxPF9eBwjwWFYKAXNAUZJYzMNctgLX8bFfftXUZEC_9t7WdOO0LtyZBCUdXaFu8pEZg95ALbIPCyvrKBOkHUhr9f8gMjBFa6Mscn5zoAQ_BA7qY9goPZEvS4jTKeg6LBY7XEhpzxQMRudB4V1Gi4PRP-FxrQ"


def main():
    login, password = LOGIN, PASSWORD
    album_id, group_id = 291217166, 220218364
    vk_sess = vk_api.VkApi(login=login, password=password)

    try:
        vk_sess.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    for image_name in os.listdir("static/img"):
        upload = vk_api.VkUpload(vk_sess)
        upload.photo("static/img/" + image_name, album_id=album_id, group_id=group_id)


if __name__ == '__main__':
    main()
