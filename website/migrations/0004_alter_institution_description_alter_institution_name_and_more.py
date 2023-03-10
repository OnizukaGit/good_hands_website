# Generated by Django 4.1.7 on 2023-02-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_institution_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'fundacja'), (1, 'organizacja pozarządowa'), (2, 'zbiórka lokalna')], default=0),
        ),
    ]
