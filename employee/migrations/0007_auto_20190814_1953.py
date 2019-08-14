# Generated by Django 2.2 on 2019-08-14 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20190814_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='emp_dept',
        ),
        migrations.AlterField(
            model_name='accomplished_by',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='accomplished_by',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.emp'),
        ),
        migrations.AlterField(
            model_name='accomplished_by',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='accomplishment',
            name='cashprice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='accomplishment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='accomplishment',
            name='highlights',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='accomplishment',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='proj_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.project'),
        ),
        migrations.AlterField(
            model_name='client_phone',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.client'),
        ),
        migrations.AlterField(
            model_name='client_phone',
            name='phone_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.emp'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='function',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='proj_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.project'),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='designation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='join_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='field',
            name='dept_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.department'),
        ),
        migrations.AlterField(
            model_name='field',
            name='descrition',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='purpose',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.emp'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='phone_no',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.emp'),
        ),
        migrations.AlterField(
            model_name='phone_no',
            name='phone_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.field'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('review', 'review'), ('close', 'close')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='designation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.emp'),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='promoted_date',
            field=models.DateField(null=True),
        ),
    ]
