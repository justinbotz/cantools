# Generated by Django 4.2.7 on 2023-11-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="media/images/"),
        ),
    ]
