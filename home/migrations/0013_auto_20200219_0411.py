# Generated by Django 2.2.5 on 2020-02-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200219_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]
