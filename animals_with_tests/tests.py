from django.test import TestCase
from django.test import Client
from rest_framework.test import APITestCase, APISimpleTestCase, force_authenticate
from django.contrib.auth.models import User
from animals.models import Family


class TestIndexView(TestCase):

    def test_view(self):
        # под гостем
        response = self.client.get('/awt/')
        self.assertEqual(response.status_code, 302)

        username = 'admin'
        password = 'admin123445'
        User.objects.create_user(username=username, password=password, email='user@adf.com')

        # под авторизованным
        self.client.login(username=username, password=password)

        response = self.client.get('/awt/')
        # код ответа
        self.assertEqual(response.status_code, 200)
        # контекст
        # print(type(response.context))
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], 'Главная страница')
        # вся страница
        print(response.content)
        self.assertIn(b'Push me', response.content)
        self.assertIn(
            b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0',
            response.content)
        self.assertIn('Главная страница'.encode(encoding='utf-8'), response.content)
        self.assertIn('Главная страница', response.content.decode(encoding='utf-8'))

        self.client.logout()

        response = self.client.get('/awt/')
        self.assertEqual(response.status_code, 302)


# api для модели Family
class TestFamilyAPI(APITestCase):

    # def setUp(self):
    #     self.clinet = CoreAPIClient

    def test_list_status_code(self):
        response = self.client.get('/awt/api/')
        self.assertEqual(response.status_code, 200)

    def test_list_data_count(self):
        names = ['Медведь', 'Тигр']
        for name in names:
            Family.objects.create(name=name)

        response = self.client.get('/awt/api/')
        self.assertEqual(len(response.json()), 2)

    def test_list_data(self):
        names = ['Медведь', 'Тигр']
        for name in names:
            Family.objects.create(name=name)

        response = self.client.get('/awt/api/')
        self.assertEqual(response.json(), [{'name': 'Медведь'}, {'name': 'Тигр'}])

    def test_create(self):
        data = {'name': 'Медведь'}
        response = self.client.post('/awt/api/', data=data)
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        family = Family.objects.create(name='Медведь')
        data = {'name': 'Ведмедь'}
        response = self.client.put(f'/awt/api/{family.id}/', data=data)
        self.assertEqual(response.status_code, 200)


class TestFamilyPermissionAPI(APITestCase):

    # def setUp(self):
    #     self.clinet = CoreAPIClient

    def test_list_status_code(self):
        response = self.client.get('/awt/api/')
        self.assertEqual(response.status_code, 200)

    def test_list_data_count(self):
        names = ['Медведь', 'Тигр']
        for name in names:
            Family.objects.create(name=name)

        response = self.client.get('/awt/permission/')
        self.assertEqual(len(response.json()), 2)

    def test_list_data(self):
        names = ['Медведь', 'Тигр']
        for name in names:
            Family.objects.create(name=name)

        response = self.client.get('/awt/permission/')
        self.assertEqual(response.json(), [{'name': 'Медведь'}, {'name': 'Тигр'}])

    def test_create(self):
        data = {'name': 'Медведь'}
        username = 'admin'
        password = 'admin123445'
        user = User.objects.create_user(username=username, password=password, email='user@adf.com')
        self.client.force_authenticate(user=user)
        response = self.client.post('/awt/permission/', data=data)
        self.assertEqual(response.status_code, 201)
    #
    def test_update(self):
        family = Family.objects.create(name='Медведь')
        data = {'name': 'Ведмедь'}

        username = 'admin'
        password = 'admin123445'
        user = User.objects.create_user(username=username, password=password, email='user@adf.com')
        self.client.force_authenticate(user=user)

        response = self.client.put(f'/awt/permission/{family.id}/', data=data)
        self.assertEqual(response.status_code, 200)

        new_family = Family.objects.get(id=family.id)
        self.assertEqual(new_family.name, 'Ведмедь')


class TestMath(APISimpleTestCase):

    def test_summ(self):
        self.assertEqual(1 + 1, 2)