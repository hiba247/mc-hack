# Generated by Django 3.2.18 on 2023-03-03 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_percontage'),
    ]

    operations = [
        migrations.CreateModel(
            name='solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solu', models.TextField()),
                ('prblm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.etat')),
            ],
        ),
    ]
