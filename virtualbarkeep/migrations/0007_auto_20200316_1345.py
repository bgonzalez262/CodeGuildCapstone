# Generated by Django 3.0.4 on 2020-03-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualbarkeep', '0006_auto_20200316_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveddrink',
            name='add_fav',
            field=models.BooleanField(default=False),
        ),
    ]
