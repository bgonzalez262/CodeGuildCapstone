# Generated by Django 3.0.4 on 2020-03-14 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('virtualbarkeep', '0002_auto_20200313_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedfood',
            name='api_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='EventItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinks', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='virtualbarkeep.SavedDrink')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='virtualbarkeep.Event')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='virtualbarkeep.SavedFood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]