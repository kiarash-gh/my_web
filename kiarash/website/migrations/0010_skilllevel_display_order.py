# Generated by Django 4.2.5 on 2023-10-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_greetings_options_alter_greetings_greeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilllevel',
            name='display_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]