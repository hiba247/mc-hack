# Generated by Django 3.2.18 on 2023-03-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
