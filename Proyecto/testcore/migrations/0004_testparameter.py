# Generated by Django 2.1.2 on 2018-11-03 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcore', '0003_testexecution_executionhash'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=240)),
                ('value', models.CharField(db_index=True, max_length=240)),
                ('type', models.CharField(db_index=True, max_length=240)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parameters', to='testcore.TestExecution')),
            ],
        ),
    ]
