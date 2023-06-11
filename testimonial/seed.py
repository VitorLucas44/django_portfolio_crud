from django_seed import Seed
from faker import Faker
from .models import Testimonial

def testimonial_run():
    seeder = Seed.seeder()
    fake = Faker()
    for _ in range(4):
        name = fake.name()
        job = fake.job()
        description = fake.text(max_nb_chars=200)

        seeder.add_entity(Testimonial, 1, {
            'name': name,
            'job': job,
            'description': description,
        })

    print(seeder.execute())