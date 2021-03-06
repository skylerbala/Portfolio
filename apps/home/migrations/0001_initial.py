# Generated by Django 2.1 on 2018-08-14 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('github_url', models.URLField()),
                ('linkedin_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField()),
                ('position', models.TextField()),
                ('description', models.TextField()),
                ('skills_used', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('company_image', models.CharField(blank=True, default='/static/images/company/', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('position', models.TextField()),
                ('skills_used', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project_image', models.CharField(blank=True, default='/static/images/personal/', max_length=500, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.TextField(choices=[('GENERAL', 'General'), ('Programming Languages', 'Programming Languages'), ('Frameworks / Libraries', 'Frameworks / Libraries'), ('Languages', 'Languages')], default='Programming Languages')),
                ('name', models.TextField()),
                ('icon', models.CharField(blank=True, default='/static/images/skills/', max_length=500, null=True)),
                ('proficiency', models.TextField(choices=[('Working Knowledge', 'Working Knowledge'), ('Proficient', 'Proficient'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], default='Proficient')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.TextField()),
                ('position', models.TextField()),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('company_image', models.CharField(blank=True, default='/static/images/company/', max_length=500, null=True)),
            ],
        ),
    ]
