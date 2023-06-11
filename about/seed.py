from django_seed import Seed
from .models import About

def run():
	seeder = Seed.seeder()
	datas = [
		{"description": "Nike", "birthday": "2023-12-12", "website": "dezaezezad", "phone": "02432342"}
	]
	for data in datas:
		seeder.add_entity(About, 1, data)
	print(seeder.execute())