# Generated by Django 3.1.4 on 2021-01-11 22:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('phone_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(61000000), django.core.validators.MaxValueValidator(65999999)])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]