# Generated by Django 3.2.18 on 2023-02-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230214_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('net', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]