# Generated by Django 3.2.18 on 2023-09-02 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20230902_1307'),
        ('monitor', '0008_auto_20230227_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarmfilterconfig',
            old_name='api',
            new_name='gateway',
        ),
        migrations.RenameField(
            model_name='alarmrecord',
            old_name='api',
            new_name='gateway',
        ),
        migrations.RenameField(
            model_name='alarmstrategy',
            old_name='api',
            new_name='gateway',
        ),
        migrations.AlterField(
            model_name='alarmfilterconfig',
            name='gateway',
            field=models.ForeignKey(blank=True, db_column='api_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.gateway'),
        ),
        migrations.AlterField(
            model_name='alarmrecord',
            name='gateway',
            field=models.ForeignKey(blank=True, db_column='api_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.gateway'),
        ),
        migrations.AlterField(
            model_name='alarmstrategy',
            name='gateway',
            field=models.ForeignKey(db_column='api_id', on_delete=django.db.models.deletion.CASCADE, to='core.gateway'),
        ),
    ]