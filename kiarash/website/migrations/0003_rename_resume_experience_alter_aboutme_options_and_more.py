# Generated by Django 4.2.5 on 2023-10-03 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contactme'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resume',
            new_name='Experience',
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'About Me', 'verbose_name_plural': 'About Me'},
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'Contact Info', 'verbose_name_plural': 'Contact Info'},
        ),
        migrations.AlterModelOptions(
            name='contactme',
            options={'verbose_name': 'Contanct Me', 'verbose_name_plural': 'Contact Me'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
        migrations.AlterModelOptions(
            name='myworks',
            options={'verbose_name': 'My Work', 'verbose_name_plural': 'My Works'},
        ),
        migrations.AlterModelOptions(
            name='skilllevel',
            options={'verbose_name': 'Skill Level', 'verbose_name_plural': 'Skill Levels'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Social Media', 'verbose_name_plural': 'Social Medias'},
        ),
    ]
