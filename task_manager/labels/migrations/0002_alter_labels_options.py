# Generated by Django 4.2 on 2023-05-23 10:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("labels", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="labels",
            options={"ordering": ["name"]},
        ),
    ]