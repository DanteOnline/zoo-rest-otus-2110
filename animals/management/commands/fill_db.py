from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from animals.models import Family, Animal, Kind, Food


class Command(BaseCommand):
    help = 'Work with db'

    def handle(self, *args, **options):
        # Удаление
        Food.objects.all().delete()
        Animal.objects.all().delete()
        Kind.objects.all().delete()
        Family.objects.all().delete()
        User.objects.all().delete()
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
        admin=User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        token = Token.objects.create(user=admin)
        print(token)

        pavel = User.objects.create_user('pavel', 'pavel@admin.com', 'admin123456')
        token = Token.objects.create(user=pavel)
        print(token)

        oleg = User.objects.create_user('oleg', 'oleg@admin.com', 'admin123456')
        token = Token.objects.create(user=oleg)
        print(token)

        group_names = ['Младшие сотрудники', 'Старшие сотрудники']
        for name in group_names:
            Group.objects.get_or_create(name=name)

        # Еще несколько видов
        names = ['Сильный', 'Красивый', 'Умный']
        for name in names:
            Kind.objects.create(name=name, family=family)

        print('done')
