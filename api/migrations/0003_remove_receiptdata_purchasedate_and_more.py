# Generated by Django 5.2.1 on 2025-05-30 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_receipt_receiptdata_points_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiptdata',
            name='purchaseDate',
        ),
        migrations.RemoveField(
            model_name='receiptdata',
            name='purchaseTime',
        ),
        migrations.RemoveField(
            model_name='receiptdata',
            name='retailer',
        ),
        migrations.RemoveField(
            model_name='receiptdata',
            name='total',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
