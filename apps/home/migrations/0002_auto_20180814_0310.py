# Generated by Django 2.1 on 2018-08-14 03:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='skills_used',
        ),
        migrations.RemoveField(
            model_name='project',
            name='skills_used',
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]