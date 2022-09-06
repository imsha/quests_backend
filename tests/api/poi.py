import requests
from faker import Faker
from faker.providers import geo

fake = Faker()
fake.add_provider(geo)


latlng = fake.latlng()

data = {
    'name': fake.name(),
    'lat': latlng[0],
    'lng': latlng[1]
}

headers = {
    'Content-Type': 'application/json'
}

r = requests.post('http://127.0.0.1:5000/poi', data=data, headers=headers)

print(r)
