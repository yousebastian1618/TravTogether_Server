# Generated by Django 3.0.5 on 2021-03-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_user_userphotourl'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userPhotoURL',
            field=models.CharField(blank=True, max_length=254, verbose_name='userPhotoURL'),
        ),
    ]