# Generated by Django 4.0 on 2021-12-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratemylawyer', '0003_remove_comment_comment_id_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
    ]
