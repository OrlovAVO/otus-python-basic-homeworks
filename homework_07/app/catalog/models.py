from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги")

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Book(models.Model):

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


    title = models.CharField('Название книги',max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    summary = models.TextField('Описание книги', max_length=1000, help_text="Введите краткое описание книги")
    isbn = models.CharField('ISBN',max_length=13, help_text='13-ти значный <a href="https://www.isbn-international.org/content/what-isbn">ISBN номер</a>')
    genre = models.ManyToManyField('Genre', help_text="Выберите жанр книги", verbose_name='Жанр')
    #pages = models.TextField('Pages', max_length=64)
    #age_limit = models.TextField('Age limit',max_length=64)

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный ID для книги в библиотеке")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Обслуживание'),
        ('o', 'Выдана'),
        ('a', 'Доступна'),
        ('r', 'Зарезервирована'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Доступность книги')

    class Meta:
        ordering = ["due_back"]
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляры книг'


    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
    first_name = models.CharField('Дата рождения', max_length=100)
    last_name = models.CharField('Дата смерти', max_length=100)
    date_of_birth = models.DateField('Родился', null=True, blank=True)
    date_of_death = models.DateField('Умер', null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
