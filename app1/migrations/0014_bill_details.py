# Generated by Django 4.1.5 on 2023-02-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_stock_allocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_item', models.CharField(max_length=100, null=True)),
                ('upto', models.CharField(max_length=100, null=True)),
                ('on_acc', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('due_date', models.DateField(max_length=100, null=True)),
                ('amount', models.IntegerField(max_length=100, null=True)),
            ],
        ),
    ]