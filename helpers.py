from faker import Faker

def generate_email():
    fake = Faker()
    username = fake.user_name()
    domain = fake.domain_name()
    return f"{username}@{domain}"

def generate_password():
    fake = Faker()
    password = fake.password(7)
    return password

def generate_username():
    fake = Faker()
    username = fake.user_name()
    return username
