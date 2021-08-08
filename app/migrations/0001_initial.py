# Generated by Django 3.2.6 on 2021-08-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(max_length=200, verbose_name='Content')),
                ('desc', models.CharField(max_length=200, verbose_name='Describe')),
            ],
            options={
                'db_table': 'medical_history',
            },
        ),
        migrations.CreateModel(
            name='PatientRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(max_length=200, verbose_name='Title')),
                ('desc', models.CharField(max_length=200, verbose_name='Title')),
            ],
            options={
                'db_table': 'patient_records',
            },
        ),
        migrations.CreateModel(
            name='TreatmentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(max_length=200, verbose_name='Content')),
                ('desc', models.CharField(max_length=200, verbose_name='Describe')),
            ],
            options={
                'db_table': 'treatment_info',
            },
        ),
    ]
