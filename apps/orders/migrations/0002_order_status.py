# Generated by Django 4.2.7 on 2023-11-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancel', 'Cancel'), ('shipped', 'Shipped')], default=10, max_length=20),
            preserve_default=False,
        ),
    ]
