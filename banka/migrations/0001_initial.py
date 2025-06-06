# Generated by Django 5.1.5 on 2025-04-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poplatky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poplatek', models.CharField(max_length=64)),
                ('vyse', models.CharField(max_length=64)),
                ('podminky', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='uroksazby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typproduktu', models.CharField(max_length=64)),
                ('splatnost', models.CharField(max_length=64)),
                ('uroksazba', models.CharField(max_length=64)),
                ('vyseuveru', models.CharField(max_length=64)),
                ('prikladsplatky', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='zakaznici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idzakaznika', models.CharField(max_length=8)),
                ('cislouctu', models.CharField(max_length=64)),
                ('typuctu', models.CharField(max_length=64)),
                ('zustatek', models.CharField(max_length=64)),
                ('mena', models.CharField(max_length=64)),
                ('datumvytvoreni', models.CharField(max_length=64)),
            ],
        ),
    ]
