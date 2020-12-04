# Generated by Django 3.1.3 on 2020-12-03 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201203_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_audio',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='question_audio',
            name='quizes',
        ),
        migrations.AddField(
            model_name='quiz',
            name='question1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.question_audio', verbose_name='Вопрос 1'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start_at',
            field=models.DateTimeField(),
        ),
    ]
