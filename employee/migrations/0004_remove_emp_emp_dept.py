# Generated by Django 2.2 on 2019-08-14 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20190814_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='emp_dept',
        ),
    ]