# Generated by Django 4.2.4 on 2023-09-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count', models.IntegerField()),
                ('date_income', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
