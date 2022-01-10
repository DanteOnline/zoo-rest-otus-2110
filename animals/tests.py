import math
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Kind, Family, Animal
from mixer.backend.django import mixer

# pytest
# unittest
class TestExample(TestCase):

    def test_pi(self):
        self.assertEqual(math.pi, 3.141592653589793)


class TestKind(TestCase):

    def setUp(self):
        # print('Я выполняюсь перед каждый тестом')
        # self.family = Family.objects.create(name='Медведь')
        # self.family = mixer.blend(Family)
        # self.kind = Kind.objects.create(name='Бурый', family=self.family)
        self.kind = mixer.blend(Kind, name='Бурый')

        # def tearDown(self):
    #     print('Я выполняюсь после каждого теста')

    def test_str(self):
        self.assertEqual(str(self.kind), 'Бурый')
        self.kind.name = '123'
        self.kind.save()

    def test_animal_count(self):
        self.assertEqual(self.kind.animal_count(), 0)
        # animal = Animal.objects.create(name='Борис', kind=self.kind)
        animal = mixer.blend(Animal, kind=self.kind)
        self.assertEqual(animal.kind.animal_count(), 1)


class TestViews(TestCase):

    def setUp(self):
        # family = Family.objects.create(name='Медведь')
        # kind = Kind.objects.create(name='Бурый', family=family)
        # self.animal = Animal.objects.create(name='Борис', kind=kind)
        self.animal = mixer.blend(Animal)

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print(response.content)
        # проверим что на странице есть
        text = response.content.decode(encoding='utf-8')
        self.assertTrue('Изменить' in text)
        self.assertTrue('class="btn btn-info"' in text)
        text_in = f'<a href="/update/{self.animal.id}/" class="btn btn-info">Изменить</a>'
        self.assertTrue(text_in in text)

        # 1. Статус код для разных пользователей
        # 2. Формы post
        # 3. Контекст
        print(response.context)
        self.assertTrue('object_list' in response.context)
        self.assertTrue('active_page' in response.context)
        self.assertEqual(response.context['active_page'], '/')

    def test_permissions(self):
        # авторизация пользователя
        admin = User.objects.create_superuser('admin', 'test@test.com', 'admin123456')
        staff = User.objects.create_user('staff', 'staff@staff.com', 'staff123456', is_staff=True)
        user = User.objects.create_user('user', 'user@staff.com', 'user123456')
        # delete/<int:pk>/
        url = f'/delete/{self.animal.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.client.login(username='admin', password='admin123456')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        self.client.login(username='staff', password='staff123456')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        url = '/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.logout()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        self.client.logout()
        self.client.login(username='admin', password='admin123456')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        self.client.login(username='user', password='user123456')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)