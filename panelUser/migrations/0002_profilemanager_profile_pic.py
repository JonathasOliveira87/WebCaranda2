# Generated by Django 4.2.6 on 2023-10-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panelUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemanager',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='img/avatar/'),
        ),
    ]
