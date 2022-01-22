# Generated by Django 3.1.7 on 2021-03-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='in_out_rp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=40)),
                ('intime', models.CharField(max_length=20)),
                ('outtime', models.CharField(max_length=20)),
                ('toggle', models.CharField(max_length=5)),
                ('date', models.DateField()),
            ],
        ),
    ]