# Generated by Django 3.2.8 on 2021-11-04 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funding', '0003_auto_20211104_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundingprogramm',
            name='who_last_updated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Letzt bearbeitet bei'),
        ),
        migrations.AlterField(
            model_name='fundingprogramm',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Letzt bearbeitet'),
        ),
    ]
