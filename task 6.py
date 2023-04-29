import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia


TOKEN = "vk1.a.e3UiV626Dz0XlG06ET2URvC0uEb0I2362oJoAMe1Z1L-nm3ZSlOIMfaKRIQxPF9eBwjwWFYKAXNAUZJYzMNctgLX8bFfftXUZEC_9t7WdOO0LtyZBCUdXaFu8pEZg95ALbIPCyvrKBOkHUhr9f8gMjBFa6Mscn5zoAQ_BA7qY9goPZEvS4jTKeg6LBY7XEhpzxQMRudB4V1Gi4PRP-FxrQ"
vk_sess = vk_api.VkApi(token=TOKEN)
vkAPI = vk_sess.get_api()
long_poll = VkLongPoll(vk_sess)


def send_message(user_id, message):
    vkAPI.messages.send(user_id=user_id, message=message, random_id=0)


def process_message(user_id):
    send_message(user_id, "What would you like to know?")

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == user_id:
            user_query = event.text

            try:
                summary = wikipedia.summary(user_query, sentences=3)
                send_message(user_id, summary)
                break
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:3]
                send_message(user_id, f"Refine your request. Options: {', '.join(options)}")
            except wikipedia.exceptions.PageError:
                send_message(user_id, "Information not found")
            except Exception:
                send_message(user_id, "Error")


def main():
    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            user_id = event.user_id
            process_message(user_id)


if __name__ == '__main__':
    main()