# Generated by Django 4.1.7 on 2023-02-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_institution_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.SmallIntegerField(choices=[('Fundacja', 'Fundacja'), ('Organizacja porządkowa', 'Organizacja pozarządowa'), ('Zbiórka lokalna', 'Zbiórka lokalna')], default='Fundacja'),
        ),
    ]