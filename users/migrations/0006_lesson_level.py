# Generated by Django 2.1.5 on 2019-01-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]