# Generated by Django 2.1.2 on 2018-11-03 17:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('testcore', '0002_auto_20180919_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='testexecution',
            name='executionhash',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
