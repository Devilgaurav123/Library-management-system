# Generated by Django 5.1.4 on 2025-03-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowedbook",
            name="returned_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
