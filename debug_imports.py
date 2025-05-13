import os
import sys
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wiki.settings')
    django.setup()
    
    # Test imports
    try:
        from Catspedia.models import Objective, Effect, Ability
        print("Models imported successfully")
        
        from Catspedia.forms import ObjectiveForm, EffectForm, AbilityForm
        print("Forms imported successfully")
        
        from Catspedia.views import (
            HomeView, SearchView,
            ObjectiveListView, ObjectiveDetailView, ObjectiveCreateView,
            ObjectiveUpdateView, ObjectiveDeleteView
        )
        print("Views imported successfully")
        
        from django.core.management import call_command
        print("Running makemigrations...")
        call_command('makemigrations')
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
