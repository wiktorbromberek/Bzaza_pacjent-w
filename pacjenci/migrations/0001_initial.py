# Generated by Django 4.1.5 on 2023-01-17 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lekarz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Notatka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Oddział',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adres', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pacjent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=12)),
                ('pesel', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Specjalizacja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specjalizacja', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wizyta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pacjenci.notatka')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacjenci.lekarz')),
                ('oddział', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacjenci.oddział')),
                ('pacjent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacjenci.pacjent')),
            ],
        ),
        migrations.AddField(
            model_name='lekarz',
            name='specjalizacja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacjenci.specjalizacja'),
        ),
    ]
