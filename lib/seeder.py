#!/usr/bin/env/ python3

from faker import Faker
import random

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Audition, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///moringa_theater.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Audition).delete()
    session.query(Role).delete()

    faker = Faker()
    
    roles = []
    for i in range(25):
        role = Role(
            character_name = faker.name(),
        )

        session.add(role)
        session.commit()
        roles.append(role)

    auditions = []
    for _ in range(50):
        role = random.choice(roles)
        audition = Audition(
            actor = faker.name(),
            location = faker.city(),
            phone = random.randint(00000000, 99999999),
            hired = 0,
            role_id = role.id,
        )
        auditions.append(audition)

    session.bulk_save_objects(auditions)
    session.commit()
    session.close()
