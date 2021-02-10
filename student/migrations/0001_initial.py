# Generated by Django 2.2.6 on 2019-12-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=20)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=20)),
                ('semail', models.EmailField(max_length=254)),
                ('scontact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]