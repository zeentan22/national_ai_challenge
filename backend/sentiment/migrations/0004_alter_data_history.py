# Generated by Django 4.1.5 on 2023-01-28 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0003_history_user_input_alter_data_aspect_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history_data', to='sentiment.history'),
        ),
    ]