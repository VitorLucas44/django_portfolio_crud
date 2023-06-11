from .models import Skill

def seed_data():
    skills = [
        {'name': 'Python', 'percent': 90},
        {'name': 'JavaScript', 'percent': 80},
        {'name': 'HTML', 'percent': 75},
        {'name': 'CSS', 'percent': 70},
    ]

    for skill_data in skills:
        skill = Skill(name=skill_data['name'], percent=skill_data['percent'])
        skill.save()

seed_data()
