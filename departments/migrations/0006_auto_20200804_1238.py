# Generated by Django 3.0.3 on 2020-08-04 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200804_1238'),
        ('departments', '0005_deanofstudents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deanofstudents',
            name='id',
        ),
        migrations.AlterField(
            model_name='deanofstudents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.Student'),
        ),
    ]
