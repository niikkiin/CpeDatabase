# Generated by Django 2.2.5 on 2020-02-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]
