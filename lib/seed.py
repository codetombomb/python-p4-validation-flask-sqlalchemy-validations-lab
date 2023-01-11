from faker import Faker
from models import Author, Post, session

fake = Faker()

for _ in range(10):
    author = Author(
        name=fake.name(),
        phone_number = fake.msisdn()
    )

    session.add(author)
    session.commit()

    


    