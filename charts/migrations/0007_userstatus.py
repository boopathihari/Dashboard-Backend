# Generated by Django 5.1.1 on 2024-10-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0006_sessiondata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_type', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
