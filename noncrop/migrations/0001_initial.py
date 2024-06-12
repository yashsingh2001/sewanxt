# Generated by Django 5.0.3 on 2024-05-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noncrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noncrop_typeofrisk', models.CharField(max_length=100)),
                ('noncrop_gender', models.CharField(max_length=10)),
                ('noncrop_ageyears', models.IntegerField()),
                ('noncrop_agemonths', models.IntegerField()),
                ('noncrop_breed', models.CharField(max_length=100)),
                ('noncrop_vaccination', models.BooleanField()),
                ('noncrop_hypothecated', models.BooleanField()),
                ('noncrop_taggingdate', models.DateField()),
                ('noncrop_suminsured', models.DecimalField(decimal_places=2, max_digits=10)),
                ('noncrop_marketvalue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('noncrop_pregnancystatus', models.CharField(max_length=100)),
                ('noncrop_calvingcycle', models.CharField(max_length=100)),
                ('noncrop_animalcolor', models.CharField(max_length=50)),
                ('noncrop_tailswitchcolour', models.CharField(max_length=50)),
                ('noncrop_lefthornshape', models.CharField(max_length=50)),
                ('noncrop_righthornshape', models.CharField(max_length=50)),
            ],
        ),
    ]
