# Generated by Django 2.0.6 on 2018-07-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_cardmember_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmember',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
