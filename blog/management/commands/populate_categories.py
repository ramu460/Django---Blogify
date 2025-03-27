
from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help = "This commands inserts cateogries data" 

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        
        Category.objects.all().delete()

        categories = ['sports', 'Technology', 'Science', 'Art', 'Food']
                   
        for category_name in categories:
            Category.objects.create(name = category_name) 
            
        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!"))
        