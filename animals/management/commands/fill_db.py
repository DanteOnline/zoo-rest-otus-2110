from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from animals.models import Family, Animal, Kind, Food


class Command(BaseCommand):
    help = 'Work with db'

    def handle(self, *args, **options):
        # Удаление
        Food.objects.all().delete()
        Animal.objects.all().delete()
        Kind.objects.all().delete()
        Family.objects.all().delete()
        # Создание
        family = Family.objects.create(name='Попугай')
        kind = Kind.objects.create(name='Бурый', family=family)
        Animal.objects.create(name='Борис', kind=kind)
        animal = Animal.objects.create(name='Миша', kind=kind)
        # Обновление
        family.name = 'Медведь'
        family.save()

        ham = Food.objects.create(name='Мясо')

        animal.foods.add(ham)
        honey = Food.objects.create(name='Мёд')
        animal.foods.add(honey)
        animal.save()

        # Создание админа
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')

        print('done')
