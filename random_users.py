import requests

response = requests.get("https://randomuser.me/api/?results=10&seed=abc")
data = response.json()


def get_users():
    users = []
    for user in data['results']:
        person = {
            'name': user['name']['first'] + " " + user['name']['last'],
            'email': user['email'],
            'place': f"{user['location']['city']}, {user['location']['country']}",
            'picture': user['picture']['large'],
            'dob': user['dob']['date'][:10]
        }
        pic_request = requests.get(person['picture'])
        with open(f"pictures/{person['dob']}.jpg", "wb") as file:
            file.write(pic_request.content)
        users.append(person)
    return users


if __name__ == '__main__':
    get_users()