# Generated by Django 3.2.25 on 2024-07-24 09:27

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20240517_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceDebugHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True)),
                ('type', models.CharField(choices=[('HTTP', 'HTTP'), ('GRPC', 'GRPC'), ('WEBSOCKET', 'WEBSOCKET')], max_length=10)),
                ('resource_name', models.CharField(max_length=32)),
                ('request_url', models.CharField(max_length=256)),
                ('request_method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE'), ('HEAD', 'HEAD'), ('OPTIONS', 'OPTIONS')], max_length=10)),
                ('request', jsonfield.fields.JSONField(blank=True, help_text='请求参数')),
                ('request_time', models.DateTimeField(blank=True, null=True)),
                ('response', jsonfield.fields.JSONField(blank=True, help_text='返回结果的内容')),
                ('status_code', models.IntegerField()),
                ('proxy_time', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spec_version', models.IntegerField()),
                ('gateway', models.ForeignKey(db_column='gateway_id', on_delete=django.db.models.deletion.CASCADE, to='core.gateway')),
                ('resource', models.ForeignKey(db_column='resource_id', on_delete=django.db.models.deletion.CASCADE, to='core.resource')),
                ('stage', models.ForeignKey(db_column='stage_id', on_delete=django.db.models.deletion.CASCADE, to='core.stage')),
            ],
            options={
                'verbose_name': 'ResourceDebugHistory',
                'verbose_name_plural': 'ResourceDebugHistory',
                'db_table': 'resource_debug_history',
            },
        ),
        migrations.RemoveField(
            model_name='sslcertificate',
            name='gateway',
        ),
        migrations.AlterUniqueTogether(
            name='sslcertificatebinding',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='sslcertificatebinding',
            name='gateway',
        ),
        migrations.RemoveField(
            model_name='sslcertificatebinding',
            name='ssl_certificate',
        ),
        migrations.RemoveField(
            model_name='stageitem',
            name='api',
        ),
        migrations.AlterUniqueTogether(
            name='stageitemconfig',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='stageitemconfig',
            name='api',
        ),
        migrations.RemoveField(
            model_name='stageitemconfig',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='stageitemconfig',
            name='stage_item',
        ),
        migrations.RemoveField(
            model_name='proxy',
            name='backend_config_type',
        ),
        migrations.RemoveField(
            model_name='proxy',
            name='backend_service',
        ),
        migrations.AlterField(
            model_name='context',
            name='type',
            field=models.CharField(choices=[('api_auth', 'Gateway auth'), ('resource_auth', 'Resource auth'), ('stage_proxy_http', 'Stage proxy http'), ('api_feature_flag', 'Gateway feature flag')], max_length=32),
        ),
        migrations.AlterField(
            model_name='publishevent',
            name='name',
            field=models.CharField(blank=True, choices=[('validata_configuration', '配置校验'), ('generate_release_task', '生成发布任务'), ('distribute_configuration', '下发配置'), ('parse_configuration', '解析配置'), ('apply_configuration', '应用配置'), ('load_configuration', '加载配置')], max_length=64),
        ),
        migrations.DeleteModel(
            name='BackendService',
        ),
        migrations.DeleteModel(
            name='SslCertificate',
        ),
        migrations.DeleteModel(
            name='SslCertificateBinding',
        ),
        migrations.DeleteModel(
            name='StageItem',
        ),
        migrations.DeleteModel(
            name='StageItemConfig',
        ),
    ]