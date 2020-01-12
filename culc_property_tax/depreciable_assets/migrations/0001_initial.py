# Generated by Django 3.0.2 on 2020-01-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevaluedRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_life', models.IntegerField()),
                ('first_year', models.DecimalField(decimal_places=3, max_digits=4)),
                ('other_year', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
    ]
