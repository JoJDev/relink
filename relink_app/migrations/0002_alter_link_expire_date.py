# Generated by Django 4.2.5 on 2023-09-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relink_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='expire_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
