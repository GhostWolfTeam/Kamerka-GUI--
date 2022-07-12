# Generated by Django 2.2.7 on 2022-07-12 03:34

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='', max_length=100)),
                ('product', models.CharField(default='', max_length=500)),
                ('org', models.CharField(default='', max_length=100, null=True)),
                ('data', models.CharField(default='', max_length=1000)),
                ('port', models.CharField(default='', max_length=10)),
                ('type', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100, null=True)),
                ('lon', models.CharField(default='', max_length=100)),
                ('lat', models.CharField(default='', max_length=100)),
                ('country_code', models.CharField(default='', max_length=100)),
                ('query', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('vulns', models.CharField(default='', max_length=100)),
                ('indicator', models.CharField(default='', max_length=100)),
                ('hostnames', models.CharField(default='', max_length=100)),
                ('screenshot', models.CharField(default='', max_length=100000)),
                ('located', models.BooleanField(default=False, null=True)),
                ('notes', models.CharField(default='', max_length=1000)),
                ('scan', models.CharField(default='', max_length=100000)),
                ('exploit', models.CharField(default='', max_length=10000)),
                ('exploited_scanned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('ics', models.CharField(max_length=100)),
                ('coordinates_search', models.CharField(max_length=1000)),
                ('nmap', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Whois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('org', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('netrange', models.CharField(max_length=100)),
                ('admin_org', models.CharField(max_length=100)),
                ('admin_email', models.CharField(max_length=100)),
                ('admin_phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterNearby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('lon', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('tweet', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
        migrations.CreateModel(
            name='ShodanScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ports', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('products', models.CharField(max_length=100)),
                ('module', models.CharField(max_length=100)),
                ('vulns', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
        migrations.CreateModel(
            name='FlickrNearby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('lon', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Dnp3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('control', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceNearby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('lon', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('port', models.CharField(max_length=100)),
                ('org', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Search'),
        ),
        migrations.CreateModel(
            name='Bosch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
        migrations.CreateModel(
            name='BinaryEdgeScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', jsonfield.fields.JSONField(default=dict)),
                ('cve', jsonfield.fields.JSONField(default=dict)),
                ('score', models.CharField(max_length=3)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kamerka.Device')),
            ],
        ),
    ]
