# Generated by Django 3.1.10 on 2021-10-28 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foerderung', '0005_foerderung_kriterienkatalog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foerderung',
            options={'verbose_name_plural': 'Förderungen'},
        ),
        migrations.RemoveField(
            model_name='foerderung',
            name='foerderprogramm_bezeichnung',
        ),
    ]
