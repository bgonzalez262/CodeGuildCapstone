# Generated by Django 3.0.4 on 2020-03-16 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtualbarkeep', '0005_event_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveddrink',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='drinks', to='virtualbarkeep.Event'),
        ),
    ]
