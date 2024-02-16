from django.test import TestCase
from django.urls import reverse
from catalog.models import Author


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('Начало setUpTestData')
        number_of_authors = 13
        for author_id in range(number_of_authors):
            Author.objects.create(first_name=f'Александр {0}'.format(author_id),
                                  last_name=f'Пушкин {0}'.format(author_id))
        print('Конец')

    def test_view_url_exists_at_desired_location(self):
        print('Начало test_view_url_exists_at_desired_location')
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)
        print('Конец test_view_url_exists_at_desired_location')

    def test_view_url_accessible_by_name(self):
        print('Начало test_view_url_accessible_by_name')
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        print('Конец test_view_url_accessible_by_name')

    def test_view_uses_correct_template(self):
        print('Начало test_view_uses_correct_template')
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_list.html')
        print('Конец test_view_uses_correct_template')

    def test_pagination_is_ten(self):
        print('Начало test_pagination_is_ten')
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['author_list']), 10)
        print('Конец test_pagination_is_ten')

    def test_lists_all_authors(self):
        print('Начало test_lists_all_authors')
        response = self.client.get(reverse('authors') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['author_list']), 3)
        print('Конец test_lists_all_authors')
