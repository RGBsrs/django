# Generated by Django 3.0.3 on 2020-02-12 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200212_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='perent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Reviews', verbose_name='родитель'),
        ),
    ]
