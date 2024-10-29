# Generated by Django 5.1.1 on 2024-10-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_poc'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunnelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_received', models.IntegerField()),
                ('poc_accepted', models.IntegerField()),
                ('poc_delivered', models.IntegerField()),
            ],
        ),
    ]
