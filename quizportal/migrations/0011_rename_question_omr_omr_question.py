# Generated by Django 3.2.5 on 2021-07-16 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizportal', '0010_omr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='omr',
            old_name='question',
            new_name='omr_question',
        ),
    ]
