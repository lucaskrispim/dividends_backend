# Generated by Django 4.0.5 on 2022-06-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0004_alter_company_dy_alter_company_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyanddividends',
            name='abbreviation',
            field=models.CharField(max_length=60, primary_key=True, serialize=False, verbose_name='abbreviation'),
        ),
    ]