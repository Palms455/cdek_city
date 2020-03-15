# Generated by Django 3.0.4 on 2020-03-15 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=15, unique=True)),
                ('city_name', models.CharField(max_length=150, null=True)),
                ('country', models.CharField(max_length=50)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='city_api.Region')),
            ],
        ),
    ]
