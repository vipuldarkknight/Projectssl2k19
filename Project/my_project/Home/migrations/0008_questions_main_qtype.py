# Generated by Django 2.2.6 on 2019-11-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_created_paper_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions_main',
            name='qtype',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
