# Generated by Django 5.1.1 on 2024-10-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_enterpriseengagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]