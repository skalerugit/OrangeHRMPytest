import string
import random


class utility:
    @staticmethod
    def generate_random_password():
        password = ''.join((random.choice(string.ascii_letters + string.digits + "!@#$%^&*()") for i in range(8)))
        return password

    @staticmethod
    def generate_random_username():
        username = ''.join((random.choice(string.ascii_letters.lower()) for i in range(8)))
        return username

