# Generated by Django 2.2 on 2019-08-14 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_remove_emp_emp_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='user',
        ),
    ]