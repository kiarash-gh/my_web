# Generated by Django 4.2.5 on 2023-10-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_merge_20231018_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
