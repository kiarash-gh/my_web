# Generated by Django 4.2.5 on 2023-10-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommender', models.CharField(max_length=255)),
                ('recommender_profile_image', models.ImageField(upload_to='recommender')),
                ('recommender_profile_url', models.URLField(blank=True, null=True)),
                ('recommendation', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
