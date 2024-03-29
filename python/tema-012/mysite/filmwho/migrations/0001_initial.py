# Generated by Django 4.1.5 on 2023-01-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=280)),
                ('run_time', models.IntegerField()),
                ('director', models.ManyToManyField(related_name='movies', to='filmwho.director')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='movie',
            field=models.ManyToManyField(related_name='directors', to='filmwho.movie'),
        ),
    ]
