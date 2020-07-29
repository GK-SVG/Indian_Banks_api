# Generated by Django 3.0.8 on 2020-07-29 11:07

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20200729_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
                ('pincode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('description', models.TextField(max_length=300)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
                ('pincode', models.CharField(max_length=10)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.State')),
            ],
        ),
        migrations.DeleteModel(
            name='PersonDeatail',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.State'),
        ),
    ]
