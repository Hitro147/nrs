# Generated by Django 3.0.5 on 2020-06-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20200624_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestitem',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]