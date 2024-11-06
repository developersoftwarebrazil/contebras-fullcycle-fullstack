# Generated by Django 5.1.2 on 2024-11-06 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_manager', '0002_rename_curse_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(default='Nome padrão', max_length=100, verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='registrationclassroom',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.classroom', verbose_name='matriculado na turma'),
        ),
        migrations.AlterField(
            model_name='registrationclassroom',
            name='registration_date',
            field=models.DateField(auto_now_add=True, verbose_name='Matriculado em'),
        ),
        migrations.AlterField(
            model_name='registrationclassroom',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.student', verbose_name='nome do aluno'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome do aluno'),
        ),
    ]