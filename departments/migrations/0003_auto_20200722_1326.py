# Generated by Django 3.0.3 on 2020-07-22 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20200719_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accomodation',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='accountsoffice',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='cateringoffice',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='headofdepartment',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='library',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='mustso',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='sportsgames',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='department_name',
        ),
    ]
