# Generated by Django 2.2.5 on 2020-06-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reductcontract', '0003_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
