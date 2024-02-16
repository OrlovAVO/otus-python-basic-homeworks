# Generated by Django 5.0.2 on 2024-02-12 15:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "date_of_death",
                    models.DateField(blank=True, null=True, verbose_name="Умер"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="Введите жанр книги", max_length=200),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "summary",
                    models.TextField(
                        help_text="Введите краткое описание книги", max_length=1000
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        help_text='13-ти значный <a href="https://www.isbn-international.org/content/what-isbn">ISBN номер</a>',
                        max_length=13,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalog.author",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        help_text="Выберите жанр книги", to="catalog.genre"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookInstance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Уникальный ID для книги в библиотеке",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("imprint", models.CharField(max_length=200)),
                ("due_back", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("m", "Maintenance"),
                            ("o", "On loan"),
                            ("a", "Available"),
                            ("r", "Reserved"),
                        ],
                        default="m",
                        help_text="Доступность книги",
                        max_length=1,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalog.book",
                    ),
                ),
            ],
            options={
                "ordering": ["due_back"],
            },
        ),
    ]