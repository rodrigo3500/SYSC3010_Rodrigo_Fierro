import requests
api_key = "https://api.thingspeak.com/channels/1161307/feeds.json?api_key=T69XHHJ0JM5DBRMM&results=2"


def get_field1():
    data = requests.get(api_key).json()
    print(data)
    field_1 = data.get("feeds")
    words = []
    for i in field_1:
        words.append(i['field1'])
    return words


print(get_field1())

