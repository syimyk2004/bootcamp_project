# Generated by Django 4.1.4 on 2022-12-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_remove_movie_hashtag_delete_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='images',
            field=models.ImageField(default=1, upload_to='movie'),
            preserve_default=False,
        ),
    ]