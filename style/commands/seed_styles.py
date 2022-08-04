import random
from click import style
from django_seed import Seed
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from style import models


class Command(BaseCommand):

    help = "This command creates products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many products you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        # categories = models.Category.objects.all()
        seeder.add_entity(
            models.Style,
            number,
            {
                # "category": lambda x: random.choice(categories),
                "user": lambda x: seeder.faker.bs(),
                "comment": lambda x: seeder.faker.sentence(),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            photo = models.Photo.objects.get(pk=pk)
            for i in range(1, random.randint(2, 3)):
                models.Photo.objects.create(
                    style=style,
                    image=f"product_photos/{random.randint(1, 35)}.webp",
                )

        self.stdout.write(self.style.SUCCESS(f"{number} products created!"))
