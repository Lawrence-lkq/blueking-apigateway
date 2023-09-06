# Generated by Django 3.2.18 on 2023-09-02 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_proxy_backend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apirelatedapp',
            old_name='api',
            new_name='gateway',
        ),
        migrations.RenameField(
            model_name='jwt',
            old_name='api',
            new_name='gateway',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='api',
            new_name='gateway',
        ),
        migrations.RenameField(
            model_name='sslcertificate',
            old_name='api',
            new_name='gateway',
        ),
        migrations.RenameField(
            model_name='sslcertificatebinding',
            old_name='api',
            new_name='gateway',
        ),
        migrations.AddField(
            model_name='resourceversion',
            name='scheme_version',
            field=models.CharField(choices=[('1.0', '旧模型版本'), ('2.0', '新模型版本')], default='1.0', max_length=32),
        ),
        migrations.AlterField(
            model_name='apirelatedapp',
            name='gateway',
            field=models.ForeignKey(db_column='api_id', on_delete=django.db.models.deletion.CASCADE, to='core.gateway'),
        ),
        migrations.AlterField(
            model_name='jwt',
            name='gateway',
            field=models.OneToOneField(db_column='api_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.gateway'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='gateway',
            field=models.ForeignKey(db_column='api_id', on_delete=django.db.models.deletion.PROTECT, to='core.gateway'),
        ),
        migrations.AlterField(
            model_name='sslcertificate',
            name='gateway',
            field=models.ForeignKey(db_column='api_id', on_delete=django.db.models.deletion.CASCADE, to='core.gateway'),
        ),
        migrations.AlterField(
            model_name='sslcertificatebinding',
            name='gateway',
            field=models.ForeignKey(db_column='api_id', on_delete=django.db.models.deletion.CASCADE, to='core.gateway'),
        ),
        migrations.AlterUniqueTogether(
            name='sslcertificatebinding',
            unique_together={('gateway', 'scope_type', 'scope_id', 'ssl_certificate')},
        ),
    ]