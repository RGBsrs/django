# Generated by Django 3.0.3 on 2020-06-13 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20200613_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Reviews', verbose_name='родитель'),
        ),
    ]
