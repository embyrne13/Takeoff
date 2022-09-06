# Generated by Django 4.1 on 2022-09-06 15:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=15)),
                ('day', models.IntegerField()),
                ('year', models.IntegerField(default=2022)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departTime', models.TimeField()),
                ('arrivalTime', models.TimeField()),
                ('airline', models.CharField(max_length=20)),
                ('duration', models.DurationField(null=True)),
                ('departDay', models.ManyToManyField(related_name='flight', to='takeoff.date')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('airport', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightDepartDate', models.DateField(blank=True, null=True)),
                ('flightArrivalDate', models.DateField(blank=True, null=True)),
                ('bookingDate', models.DateTimeField(default=datetime.datetime.now)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=13)),
                ('flightFare', models.FloatField(blank=True, null=True)),
                ('refNumber', models.CharField(max_length=5, unique=True)),
                ('flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='takeoff.flight')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='takeoff.user')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=20)),
                ('lastName', models.CharField(blank=True, max_length=20)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='takeoff.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='takeoff.user')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='takeoff.place'),
        ),
        migrations.AddField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='takeoff.place'),
        ),
    ]
