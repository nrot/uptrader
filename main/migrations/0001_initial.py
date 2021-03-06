# Generated by Django 2.0.3 on 2018-05-25 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itemMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('parentItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.itemMenu')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='parentMenu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Menu'),
        ),
    ]
