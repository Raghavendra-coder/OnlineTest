# Generated by Django 3.2.5 on 2021-07-16 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizportal', '0013_auto_20210716_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponses',
            name='attempt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='quizportal.userattempts'),
        ),
    ]