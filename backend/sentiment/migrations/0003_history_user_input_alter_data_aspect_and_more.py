# Generated by Django 4.1.5 on 2023-01-28 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0002_alter_data_aspect'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='user_input',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='aspect',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='history',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history_data', to='sentiment.history'),
        ),
    ]
