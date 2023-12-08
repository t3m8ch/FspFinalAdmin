# Generated by Django 5.0 on 2023-12-08 21:44

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0006_alter_course_course_age_alter_course_value_lesson_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forward',
            options={'verbose_name': 'Вид угрозы', 'verbose_name_plural': 'Виды угроз'},
        ),
        migrations.AlterModelOptions(
            name='forwardsrc',
            options={'verbose_name': 'Угроза -> media', 'verbose_name_plural': 'Угроза -> media'},
        ),
        migrations.AlterModelOptions(
            name='lessontype',
            options={'verbose_name': 'Тип урока', 'verbose_name_plural': 'Типы уроков'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='value',
        ),
        migrations.CreateModel(
            name='LessonMat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('lesson_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminka.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Материал урока',
                'verbose_name_plural': 'Материалы урока',
            },
        ),
        migrations.CreateModel(
            name='LessonMatSrc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.CharField(max_length=255, verbose_name='S3 картинка')),
                ('lesson_mat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminka.lessonmat', verbose_name='Материал урока')),
            ],
            options={
                'verbose_name': 'Материал урока -> media',
                'verbose_name_plural': 'Материал урока -> media',
            },
        ),
    ]