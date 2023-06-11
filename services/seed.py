from django_seed import Seed
from .models import Services

def services_run():
    seeder = Seed.seeder()
    datas = [
        {"title_services": "Service 1", "descriptions": "Description 1", "icon": "bi-briefcase"},
        {"title_services": "Service 2", "descriptions": "Description 2", "icon": "bi-card-checklist"},
        {"title_services": "Service 3", "descriptions": "Description 3", "icon": "bi-bar-chart"},
        {"title_services": "Service 4", "descriptions": "Description 4", "icon": "bi-binoculars"},
        {"title_services": "Service 5", "descriptions": "Description 5", "icon": "bi-brightness-high"},
        {"title_services": "Service 6", "descriptions": "Description 6", "icon": "bi-calendar4-week"},
    ]
    for data in datas:
        seeder.add_entity(Services, 1, data)
    print(seeder.execute())