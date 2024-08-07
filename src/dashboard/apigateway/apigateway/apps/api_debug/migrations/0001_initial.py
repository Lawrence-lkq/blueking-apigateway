# Generated by Django 3.2.25 on 2024-07-26 02:51

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0040_auto_20240517_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIDebugHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True)),
                ('resource_name', models.CharField(help_text='资源名称', max_length=32)),
                ('request', jsonfield.fields.JSONField(blank=True, help_text='请求参数')),
                ('response', jsonfield.fields.JSONField(blank=True, help_text='返回结果')),
                ('gateway', models.ForeignKey(db_column='gateway_id', on_delete=django.db.models.deletion.CASCADE, to='core.gateway')),
                ('stage', models.ForeignKey(db_column='stage_id', on_delete=django.db.models.deletion.CASCADE, to='core.stage')),
            ],
            options={
                'verbose_name': 'APIDebugHistory',
                'verbose_name_plural': 'APIDebugHistory',
                'db_table': 'api_debug_history',
            },
        ),
    ]
