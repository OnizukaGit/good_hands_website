# Generated by Django 4.1.7 on 2023-03-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
