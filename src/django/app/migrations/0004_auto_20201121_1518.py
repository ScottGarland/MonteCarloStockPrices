# Generated by Django 3.1.3 on 2020-11-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201121_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
