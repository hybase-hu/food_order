# Generated by Django 3.2 on 2021-07-30 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('description', models.TextField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles_selected_food', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('deliver_location_city', models.CharField(max_length=100)),
                ('deliver_location_street', models.CharField(max_length=100)),
                ('deliver_location_zip', models.IntegerField()),
                ('comment', models.TextField()),
                ('payed_method', models.CharField(choices=[('#1', 'CASH'), ('#2', 'WITH CREDIT CARD')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('foods', models.ManyToManyField(to='orders.SelectedFood')),
            ],
        ),
    ]