# Generated by Django 5.0.3 on 2024-03-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('income_balance', models.CharField(blank=True, choices=[('Income Statement', 'Income Statement'), ('Balance sheet', 'Balance Sheet')], max_length=255, null=True, verbose_name='Income/Balance')),
                ('accountcategory', models.CharField(choices=[('Assest', 'Assest'), ('Liability', 'Liability'), ('Equity', 'Equity'), ('Income', 'Income'), ('Expense', 'Expense')], max_length=255, verbose_name='Account Category')),
                ('debit_credit', models.CharField(choices=[('Both', 'Both'), ('Debit', 'Debit'), ('Credit', 'Credit')], max_length=10, verbose_name='Debit/Credit')),
                ('accounttype', models.CharField(choices=[('Posting', 'Posting'), ('Heading', 'Heading'), ('Total', 'Total'), ('Begin-Total', 'Begin-Total'), ('End-Total', 'End-Total')], max_length=255, verbose_name='Account Type')),
                ('balance', models.FloatField(verbose_name='Balance')),
            ],
        ),
        migrations.CreateModel(
            name='GLAccountCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('account_category', models.CharField(choices=[('Assest', 'Assest'), ('Liability', 'Liability'), ('Equity', 'Equity'), ('Income', 'Income'), ('Expense', 'Expense')], max_length=255)),
                ('balance', models.IntegerField()),
            ],
            options={
                'verbose_name': 'G/L Account Category',
                'verbose_name_plural': 'G/L Account Categories',
            },
        ),
    ]
