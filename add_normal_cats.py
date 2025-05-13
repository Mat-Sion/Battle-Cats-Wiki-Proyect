import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wiki.settings')
django.setup()

from Catspedia.models import ClassType, EvolutionCat

def create_normal_cats():
    # Create Normal Class Type
    normal_class, created = ClassType.objects.get_or_create(
        name='Normal Cats',
        defaults={
            'description': 'The basic cats that form the foundation of your army. These cats can be obtained through regular gameplay and upgraded through the upgrade menu.',
            'rarity': 'NORMAL'
        }
    )
    if created:
        print("Created Normal Cat class type")
    else:
        print("Normal Cat class type already exists")

    # List of all normal cats with their evolutions
    normal_cats = [
        {
            'base_name': 'Cat',
            'forms': [
                ('Basic Cat', 'A normal cat. Not very strong, but cheap to produce.'),
                ('Macho Cat', 'A more masculine cat. Higher health than Basic Cat.'),
                ('Mohawk Cat', 'A cat with attitude. Even higher health and attack power.')
            ],
            'stats': {
                'base_health': [400, 500, 600],
                'base_attack': [100, 120, 140],
                'attack_range': 140,
                'movement_speed': 10,
                'knockbacks': 4,
                'attack_frequency': 1.0,
                'cost': 75,
                'recharge_time': 2.0,
            }
        },
        {
            'base_name': 'Tank',
            'forms': [
                ('Tank Cat', 'High health but low attack power. Perfect for taking hits.'),
                ('Wall Cat', 'Even more health! Great for defensive strategies.'),
                ('Eraser Cat', 'Ultimate defense unit. Extremely high health!')
            ],
            'stats': {
                'base_health': [800, 1000, 1200],
                'base_attack': [60, 70, 80],
                'attack_range': 130,
                'movement_speed': 8,
                'knockbacks': 3,
                'attack_frequency': 1.27,
                'cost': 100,
                'recharge_time': 3.0,
            }
        },
        {
            'base_name': 'Axe',
            'forms': [
                ('Axe Cat', 'High attack power but low health. Good for dealing damage.'),
                ('Dark Cat', 'Even higher attack power. A strong offensive unit.'),
                ('Islander Cat', 'Maximum attack power. The ultimate offensive normal cat!')
            ],
            'stats': {
                'base_health': [300, 350, 400],
                'base_attack': [240, 280, 320],
                'attack_range': 140,
                'movement_speed': 8,
                'knockbacks': 4,
                'attack_frequency': 1.3,
                'cost': 300,
                'recharge_time': 4.87,
            }
        },
        {
            'base_name': 'Gross',
            'forms': [
                ('Gross Cat', 'Long-range attacker. Can hit enemies from a safe distance.'),
                ('Sexy Legs Cat', 'Longer range and higher attack power.'),
                ('Macho Legs Cat', 'Maximum power long-range attacker!')
            ],
            'stats': {
                'base_health': [200, 250, 300],
                'base_attack': [180, 200, 220],
                'attack_range': 200,
                'movement_speed': 8,
                'knockbacks': 3,
                'attack_frequency': 1.4,
                'cost': 400,
                'recharge_time': 5.23,
            }
        },
        {
            'base_name': 'Cow',
            'forms': [
                ('Cow Cat', 'Fast-moving unit. Good for quick attacks.'),
                ('Giraffe Cat', 'Even faster movement speed!'),
                ('Lion Cat', 'Lightning-fast movement and high damage!')
            ],
            'stats': {
                'base_health': [200, 240, 280],
                'base_attack': [120, 140, 160],
                'attack_range': 140,
                'movement_speed': 16,
                'knockbacks': 4,
                'attack_frequency': 1.2,
                'cost': 350,
                'recharge_time': 4.0,
            }
        },
        {
            'base_name': 'Bird',
            'forms': [
                ('Bird Cat', 'Flying unit that can attack floating enemies.'),
                ('UFO Cat', 'Faster attack rate and higher damage.'),
                ('The Flying Cat', 'Ultimate flying unit with massive damage!')
            ],
            'stats': {
                'base_health': [160, 200, 240],
                'base_attack': [200, 240, 280],
                'attack_range': 250,
                'movement_speed': 9,
                'knockbacks': 4,
                'attack_frequency': 0.5,
                'cost': 450,
                'recharge_time': 7.0,
            }
        },
        {
            'base_name': 'Fish',
            'forms': [
                ('Fish Cat', 'Strong against Red enemies. High damage.'),
                ('Whale Cat', 'Even stronger against Red enemies!'),
                ('Island Cat', 'Massive damage against Red enemies!')
            ],
            'stats': {
                'base_health': [280, 320, 360],
                'base_attack': [400, 440, 480],
                'attack_range': 140,
                'movement_speed': 8,
                'knockbacks': 4,
                'attack_frequency': 1.87,
                'cost': 500,
                'recharge_time': 6.87,
            }
        },
        {
            'base_name': 'Lizard',
            'forms': [
                ('Lizard Cat', 'Very long range attacker. High damage.'),
                ('Dragon Cat', 'Even longer range and higher damage!'),
                ('King Dragon Cat', 'Ultimate long-range attacker!')
            ],
            'stats': {
                'base_health': [200, 240, 280],
                'base_attack': [300, 340, 380],
                'attack_range': 400,
                'movement_speed': 8,
                'knockbacks': 3,
                'attack_frequency': 2.0,
                'cost': 600,
                'recharge_time': 8.0,
            }
        },
        {
            'base_name': 'Titan',
            'forms': [
                ('Titan Cat', 'Very strong unit with high health and attack.'),
                ('Mythical Titan Cat', 'Even stronger with chance of critical hits!'),
                ('Jamiera Cat', 'Ultimate strong unit with guaranteed critical hits!')
            ],
            'stats': {
                'base_health': [1000, 1200, 1400],
                'base_attack': [450, 500, 550],
                'attack_range': 140,
                'movement_speed': 8,
                'knockbacks': 2,
                'attack_frequency': 2.53,
                'cost': 1200,
                'recharge_time': 10.0,
            }
        },
    ]

    # Create all cats
    for cat in normal_cats:
        for i, (name, description) in enumerate(cat['forms'], 1):
            cat_data = {
                'name': name,
                'description': description,
                'class_type': normal_class,
                'evolution_level': i,
                'base_health': cat['stats']['base_health'][i-1],
                'base_attack': cat['stats']['base_attack'][i-1],
                'attack_range': cat['stats']['attack_range'],
                'movement_speed': cat['stats']['movement_speed'],
                'knockbacks': cat['stats']['knockbacks'],
                'attack_frequency': cat['stats']['attack_frequency'],
                'cost': cat['stats']['cost'],
                'recharge_time': cat['stats']['recharge_time'],
                'target_types': 'All Types',
                'abilities': f'Base form of {cat["base_name"]} Cat series' if i == 1 else f'Evolution {i} of {cat["base_name"]} Cat'
            }
            
            cat_obj, created = EvolutionCat.objects.get_or_create(
                name=name,
                defaults=cat_data
            )
            if created:
                print(f"Created {name}")
            else:
                print(f"{name} already exists")

if __name__ == '__main__':
    print("Creating Normal Cats...")
    create_normal_cats()
    print("Done!")