# Generated by Django 4.1.7 on 2023-03-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=2000, null=True)),
                ('address', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]