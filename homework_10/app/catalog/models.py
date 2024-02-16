import uuid
from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги")

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Book(models.Model):

    class Meta:
        ordering = ['-id']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


    title = models.CharField('Название книги',max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True,
                               verbose_name='Автор')
    summary = models.TextField('Описание книги', max_length=1000,
                               help_text="Введите краткое описание книги")
    isbn = models.CharField('ISBN',max_length=13,
                            help_text='13-ти значный '
                                      '<a href='
                                      '"https://www.isbn-international.org/content/what-isbn">'
                                      'ISBN номер</a>')
    genre = models.ManyToManyField('Genre', help_text="Выберите жанр книги", verbose_name='Жанр')


    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID для книги в библиотеке")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, verbose_name='Книга')
    due_back = models.DateField(null=True, blank=True, verbose_name='Возврат:')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True, verbose_name='Взял')

    LOAN_STATUS = (
        ('Н', 'Недоступна'),
        ('В', 'Выдана'),
        ('Д', 'Доступна'),
        ('З', 'Зарезервирована'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='Д',
                              help_text='Доступность книги', verbose_name='Статус:')

    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    class Meta:
        ordering = ["due_back"]
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляры книг'


    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    date_of_death = models.DateField('Дата смерти', null=True, blank=True)

    class Meta:
        ordering = ['last_name',
                    'first_name'
                    ]
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
