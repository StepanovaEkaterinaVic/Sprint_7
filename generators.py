from faker import Faker
import random


fake = Faker()


def generate_courier_body():
    return {
        "login": fake.word()+fake.word(),
        "password": fake.random_int(min=1000, max=9999),
        "firstname": fake.first_name()
    }


def generate_order_body(color_scooter):
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.street_name(),
        "metroStation": fake.random_int(min=1, max=215),
        "phone": '+7' + ''.join([str(random.randint(0, 9)) for _ in range(10)]),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date_between(start_date='+1d', end_date='+30d').isoformat(),
        "comment": fake.word(),
        "color": color_scooter
    }
