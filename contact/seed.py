from django_seed import Seed
from .models import Contact

def contact_run():
    seeder = Seed.seeder()
    datas = [
        {"email": "john@example.com", "phone": "1234567890", "adress": "123 Main St"},
    ]
    for data in datas:
        seeder.add_entity(Contact, 1, data)
    print(seeder.execute())