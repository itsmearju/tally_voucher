# Generated by Django 4.1.5 on 2023-02-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_party_details_invoice_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
