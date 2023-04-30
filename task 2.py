import vk_api


def main():
    login, password = LOGIN, PASSWORD
    vk_sess = vk_api.VkApi(login, password)
    try:
        vk_sess.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vkAPI = vk_sess.get_api()

    friends = vkAPI.friends.get(fields="bdate")
    if friends['items']:
        answer = []
        for user in friends['items']:
            data = {"first_name": user["first_name"],
                    "last_name": user["last_name"]}
            if "bdate" in user:
                data["date"] = user["bdate"]
            else:
                data["date"] = "дата рождения не указана"
            answer.append(data)
        answer.sort(key=lambda x: x["last_name"])
        for friend in answer:
            print(friend["last_name"], friend["first_name"], friend["date"])


if __name__ == '__main__':
    main()