# Generated by Django 4.1.3 on 2022-11-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_alter_comentario_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]