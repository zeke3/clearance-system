# Generated by Django 3.0.3 on 2020-08-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_student_cleared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentofficer',
            name='department_name',
            field=models.CharField(choices=[('Library', 'Library'), ('Workshop', 'Workshop'), ('MustSo', 'MustSo'), ('Laboratories', 'Laboratories'), ('Head Of Department', 'Head Of Department'), ('Catering Office', 'Catering Office'), ('Sports and Games', 'Sports and Games'), ('Accomodation', 'Accomodation'), ('Accounts Office', 'Accounts Office'), ('Dean Of Students', 'Dean Of Students')], max_length=100),
        ),
    ]
