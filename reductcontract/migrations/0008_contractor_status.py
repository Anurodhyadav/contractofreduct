# Generated by Django 3.0.7 on 2020-06-18 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reductcontract', '0007_remove_contractor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='status',
            field=models.TextField(null=True),
        ),
    ]