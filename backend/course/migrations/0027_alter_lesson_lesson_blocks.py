# Generated by Django 4.1.5 on 2023-04-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_merge_20230401_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_blocks',
            field=models.ManyToManyField(blank=True, choices=[(1, 'Block TItle'), (2, 'Second block'), (3, 'Third block title')], related_name='lesson_blocks', to='course.lessonblock'),
        ),
    ]