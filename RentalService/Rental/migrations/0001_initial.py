# Generated by Django 2.2.3 on 2020-04-14 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('code', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('street', models.CharField(max_length=120)),
                ('street2', models.CharField(max_length=120)),
                ('zip', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=120)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.CountryModel')),
            ],
        ),
        migrations.CreateModel(
            name='RentalAgreementModel',
            fields=[
                ('reference', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('rental_amount', models.FloatField()),
                ('period', models.IntegerField()),
                ('period_length', models.IntegerField()),
                ('rental_type', models.CharField(max_length=50)),
                ('agreement_date', models.DateField()),
                ('item', models.CharField(max_length=60)),
                ('stage', models.CharField(max_length=50)),
                ('custoemer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.CustomerModel')),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('code', models.CharField(max_length=5, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.CountryModel')),
            ],
        ),
        migrations.CreateModel(
            name='RentalRegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=25, unique=True)),
                ('payment_date', models.DateField()),
                ('payment_amount', models.FloatField()),
                ('rental_type', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=120)),
                ('stage', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.CustomerModel')),
                ('rental_agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.RentalAgreementModel')),
            ],
        ),
        migrations.CreateModel(
            name='RentalAgreementLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('payment_amount', models.FloatField()),
                ('status', models.CharField(max_length=50)),
                ('rental_agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.RentalAgreementModel')),
            ],
        ),
        migrations.AddField(
            model_name='customermodel',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.StateModel'),
        ),
    ]