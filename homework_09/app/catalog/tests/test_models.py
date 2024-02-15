from django.test import TestCase

# Create your tests here.

from catalog.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('Начало setUpTestData')
        Author.objects.create(first_name='Big', last_name='Bob')
        print('Конец setUpTestData')

    def test_first_name_label(self):
        print('Начало test_first_name_label')
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'Имя')
        print('Конец test_first_name_label')

    def test_last_name_label(self):
        print('Начало test_last_name_label')
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'Фамилия')
        print('Конец test_last_name_label')

    def test_date_of_birth_label(self):
        print('Начало test_date_of_birth_label')
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'Дата рождения')
        print('Конец test_date_of_birth_label')

    def test_date_of_death_label(self):
        print('Начало test_date_of_death_label')
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Дата смерти')
        print('Конец test_date_of_death_label')

    def test_first_name_max_length(self):
        print('Начало test_first_name_max_length')
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)
        print('Конец test_first_name_max_length')

    def test_last_name_max_length(self):
        print('Начало test_last_name_max_length')
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)
        print('Конец test_last_name_max_length')

    def test_object_name_is_last_name_comma_first_name(self):
        print('Начало test_object_name_is_last_name_comma_first_name')
        author = Author.objects.get(id=1)
        expected_object_name = '{0}, {1}'.format(author.last_name, author.first_name)
        self.assertEqual(str(author), expected_object_name)
        print('Конец test_object_name_is_last_name_comma_first_name')

    def test_get_absolute_url(self):
        print('Начало test_get_absolute_url')
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/authors/1')
        print('Конец test_get_absolute_url')