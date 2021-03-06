# Generated by Django 4.0 on 2021-12-18 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('article_number', models.CharField(max_length=13)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('unit', models.CharField(choices=[('gr', 'grams'), ('kg', 'kilograms'), ('cl', 'centiliter'), ('l', 'liter')], default='gr', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipager.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.ManyToManyField(through='recipager.Item', to='recipager.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipager.recipe'),
        ),
    ]
