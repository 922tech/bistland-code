from django.urls import reverse
from django.contrib.auth import get_user_model

from common.tests import BaseTestCase
from .models import Titanic


class TitanicViewsTestCase(BaseTestCase):

    def setUp(self):
        # Create a user if you have authentication
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

        # Sample data for Titanic
        self.titanic_data = {
            'passengerID': 1,
            'survived': 1,
            'pclass': 1,
            'name': 'John Doe',
            'sex': 'male',
            'age': 22,
            'sibsp': 1,
            'parch': 0,
            'ticket': 'A/5 21171',
            'fare': 7.25,
            'cabin': 'C85',
            'embarked': 'C'
        }
        self.titanic = Titanic.objects.create(**self.titanic_data)

    def test_titanic_list_view(self):
        response = self.client.get(reverse('titanic_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'titanic_list.html')
        self.assertContains(response, self.titanic.name)

    def test_titanic_create_view(self):
        response = self.client.get(reverse('titanic_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'titanic_form.html')

        response = self.client.post(reverse('titanic_create'), data={
            'passengerID': 2,
            'survived': 0,
            'pclass': 3,
            'name': 'Jane Doe',
            'sex': 'female',
            'age': 28,
            'sibsp': 0,
            'parch': 1,
            'ticket': 'C123',
            'fare': 15.00,
            'cabin': 'C123',
            'embarked': 'S'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        self.assertTrue(Titanic.objects.filter(name='Jane Doe').exists())

    def test_titanic_update_view(self):
        response = self.client.get(reverse('titanic_edit', kwargs={'pk': self.titanic.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'titanic_form.html')

        response = self.client.post(reverse('titanic_edit', kwargs={'pk': self.titanic.pk}), data={
            'passengerID': self.titanic.passengerID,
            'survived': 0,  # Change the survived status
            'pclass': self.titanic.pclass,
            'name': self.titanic.name,
            'sex': self.titanic.sex,
            'age': self.titanic.age,
            'sibsp': self.titanic.sibsp,
            'parch': self.titanic.parch,
            'ticket': self.titanic.ticket,
            'fare': self.titanic.fare,
            'cabin': self.titanic.cabin,
            'embarked': self.titanic.embarked
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful update
        self.titanic.refresh_from_db()
        self.assertEqual(self.titanic.survived, 0)

    def test_titanic_delete_view(self):
        response = self.client.get(reverse('titanic_delete', kwargs={'pk': self.titanic.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'titanic_confirm_delete.html')

        response = self.client.post(reverse('titanic_delete', kwargs={'pk': self.titanic.pk}))
        self.assertEqual(response.status_code, 302)  # Redirects after successful deletion
        self.assertFalse(Titanic.objects.filter(pk=self.titanic.pk).exists())

    def test_titanic_table_view(self):
        response = self.client.get(reverse('titanic_table'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'titanic_table.html')
        self.assertContains(response, self.titanic.name)
