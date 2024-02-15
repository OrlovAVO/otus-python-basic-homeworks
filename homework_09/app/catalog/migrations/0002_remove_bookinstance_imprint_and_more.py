# Generated by Django 5.0.2 on 2024-02-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookinstance",
            name="imprint",
        ),
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("m", "Обслуживание"),
                    ("o", "Выдана"),
                    ("a", "Доступна"),
                    ("r", "Зарезервирована"),
                ],
                default="m",
                help_text="Доступность книги",
                max_length=1,
            ),
        ),
    ]
