# Generated by Django 4.0.4 on 2022-06-03 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nestedm2m', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('directions', models.TextField()),
                ('ingredients', models.ManyToManyField(to='nestedm2m.ingredient')),
            ],
        ),
    ]