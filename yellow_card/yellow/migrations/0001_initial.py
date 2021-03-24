# Generated by Django 3.1.7 on 2021-03-21 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('issue_date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('immunised_for', models.CharField(choices=[('YF ', 'Yellow Fever'), ('Ot', 'Others')], max_length=45)),
                ('passport_or_nin_number', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='pic')),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
    ]
