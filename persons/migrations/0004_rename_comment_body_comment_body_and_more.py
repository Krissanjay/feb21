# Generated by Django 4.2.9 on 2024-02-15 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_rename_product_comment_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commenter_name',
            new_name='name',
        ),
    ]
