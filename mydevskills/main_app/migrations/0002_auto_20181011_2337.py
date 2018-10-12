# Generated by Django 2.1.1 on 2018-10-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_level',
            field=models.IntegerField(choices=[('1', 'Fundamental Awareness'), ('2', 'Novice'), ('3', 'Intermediate'), ('4', 'Advanced'), ('5', 'Expert')], default='1'),
        ),
    ]