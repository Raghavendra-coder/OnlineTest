# Generated by Django 3.2.5 on 2021-07-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizportal', '0004_rename_quiz_question_select_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]