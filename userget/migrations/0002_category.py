# Generated by Django 4.2.6 on 2023-10-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
