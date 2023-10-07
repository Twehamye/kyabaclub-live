# Generated by Django 4.1.2 on 2023-08-03 22:54

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=300)),
                ('asset_desc', models.TextField()),
                ('purchase_amount', models.PositiveIntegerField()),
                ('date_of_purchase', models.DateTimeField()),
                ('document', models.ImageField(blank=True, upload_to='deposits/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('paid', 'paid'), ('unpaid', 'unpaid')], default='unpaid', max_length=300)),
                ('issue_date', models.DateField()),
                ('clearance_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today)])),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('nin', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=500)),
                ('sex', models.CharField(choices=[('Male', 'male'), ('Female', 'Female')], max_length=10)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Windowed', 'Windowed'), ('Divorsed', 'Divorsed')], max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.PositiveIntegerField(default=0)),
                ('date_of_birth', models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date.today)])),
                ('current_address', models.CharField(max_length=300)),
                ('home_address', models.CharField(max_length=300)),
                ('Registered_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spouse_name', models.CharField(max_length=200)),
                ('spouse_telephone', models.PositiveIntegerField()),
                ('father_name', models.CharField(max_length=200)),
                ('father_telephone', models.PositiveIntegerField()),
                ('mother_name', models.CharField(max_length=200)),
                ('mother_telephone', models.PositiveIntegerField()),
                ('number_of_children', models.PositiveIntegerField()),
                ('next_of_kin_name', models.CharField(max_length=200)),
                ('next_of_kin_telephone', models.IntegerField()),
                ('next_of_kin_relationship', models.CharField(max_length=200)),
                ('beneficiary_name', models.CharField(max_length=200)),
                ('beneficiary_telephone', models.PositiveIntegerField()),
                ('beneficiary_relationship', models.CharField(max_length=200)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kyaclub_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='FinePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('fine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kyaclub_app.fine')),
            ],
        ),
        migrations.AddField(
            model_name='fine',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kyaclub_app.member'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=300)),
                ('amount', models.PositiveIntegerField()),
                ('date_of_expense', models.DateTimeField()),
                ('receipt', models.ImageField(blank=True, upload_to='deposits/%Y/%m/%d')),
                ('member_responsible', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='kyaclub_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('purpose', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('deposited_by', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('Approved', 'Approved'), ('Rejeted', 'Rejected')], default='pending', max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('receipt', models.ImageField(blank=True, upload_to='deposits/%Y/%m/%d')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kyaclub_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='ChildrenDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=300)),
                ('date_of_birth', models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date.today)])),
                ('Registered_date', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kyaclub_app.member')),
            ],
        ),
    ]
