# Generated by Django 4.0 on 2021-12-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_transaction_username_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Travel', 'Travel'), ('Investment', 'Investment'), ('Shopping', 'Shopping'), ('Learning', 'Learning'), ('Fees', 'Fees'), ('Other', 'Other')], default='oth', max_length=10),
        ),
    ]
