# Generated by Django 2.2 on 2021-06-22 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('street', models.CharField(blank=True, max_length=64, null=True)),
                ('adress', models.PositiveIntegerField(blank=True, null=True)),
                ('room', models.PositiveIntegerField(blank=True, null=True)),
                ('m2', models.PositiveIntegerField(blank=True, null=True)),
                ('pool', models.BooleanField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ['published'],
            },
        ),
    ]
