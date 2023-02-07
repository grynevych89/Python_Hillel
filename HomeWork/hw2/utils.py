from faker import Faker
import requests

fake = Faker()


def requirements():
    req = open('requirements.txt', 'r')
    return req


def generate_users():
    num = 100
    items = [f'{fake.name()} + {fake.email()}' for _ in range(num)]
    print(items)
    return items


def space():
    headers = {'Accept': 'application/json'}
    r = requests.get('http://api.open-notify.org/astros.json', headers=headers)
    r = r.json()
    print(r)
    return r

