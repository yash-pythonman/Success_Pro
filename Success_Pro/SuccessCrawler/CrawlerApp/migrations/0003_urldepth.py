# Generated by Django 2.2.2 on 2019-07-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrawlerApp', '0002_auto_20190718_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlDepth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('depth', models.IntegerField(max_length=10)),
            ],
        ),
    ]