# Generated by Django 2.0 on 2018-08-12 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Run', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='run',
            options={'ordering': ['-time']},
        ),
    ]
