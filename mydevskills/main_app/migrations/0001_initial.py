# Generated by Django 2.1.1 on 2018-10-11 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('skill_level', models.IntegerField(choices=[('1', 'Fundamental Awareness'), ('2', 'Novice'), ('3', 'Intermediate'), ('4', 'Advanced'), ('5', 'Expert')], default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.User'),
        ),
        migrations.AddField(
            model_name='note',
            name='skill_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Skill'),
        ),
    ]
