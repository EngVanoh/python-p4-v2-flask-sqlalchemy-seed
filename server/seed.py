#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet
from faker import Faker

fake = Faker()

with app.app_context():
    Pet.query.delete()

    # Create an empty list
    pets = []
    species = ["Dog", "Cat", "Hamster", "Snake"]

    # Add some Pet instances to the list
    pets.append(Pet(name = "Fido", species = "Dog"))
    pets.append(Pet(name = "Whiskers", species = "Cat"))
    pets.append(Pet(name = "Hermie", species = "Hamster"))
    pets.append(Pet(name = "Slither", species = "Snake"))

    for n in range(10):
        pets.append(Pet(name = fake.first_name(), species = fake.random_element(elements=species)))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()