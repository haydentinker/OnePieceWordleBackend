# Generated by Django 4.2 on 2023-05-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onepiece", "0002_remove_character_manage_debut_character_birthday_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="url",
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
