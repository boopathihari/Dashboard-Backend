# Generated by Django 5.1.1 on 2024-10-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_connectionrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='POC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
