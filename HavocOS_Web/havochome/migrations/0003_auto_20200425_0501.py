# Generated by Django 3.0.2 on 2020-04-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havochome', '0002_auto_20200425_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='Role',
            field=models.CharField(max_length=100, null=True),
        ),
    ]