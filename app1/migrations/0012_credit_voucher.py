# Generated by Django 4.1.5 on 2023-02-01 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_new_buyer_addr_new_buyer_bill_to_new_buyer_contr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='credit_voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vou_id', models.IntegerField(null=True)),
                ('party_nm', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('led_account', models.CharField(max_length=255, null=True)),
                ('item_nm', models.CharField(max_length=255, null=True)),
                ('quant', models.IntegerField(null=True)),
                ('rate', models.IntegerField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('narration', models.CharField(max_length=255, null=True)),
                ('voucher_de', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.voucher')),
            ],
        ),
    ]
