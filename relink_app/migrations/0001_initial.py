# Generated by Django 4.2.5 on 2023-09-26 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='title', max_length=50)),
                ('slug', models.SlugField(default='')),
                ('url', models.URLField(default='')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateTimeField(default=datetime.datetime(2023, 9, 26, 16, 44, 5, 118378))),
                ('public', models.BooleanField(default=True)),
            ],
        ),
    ]
