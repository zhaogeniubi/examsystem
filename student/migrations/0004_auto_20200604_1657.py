# Generated by Django 2.1 on 2020-06-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200604_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('3', 'difficult'), ('2', 'general'), ('1', 'easy')], max_length=10, verbose_name='等级'),
        ),
    ]
