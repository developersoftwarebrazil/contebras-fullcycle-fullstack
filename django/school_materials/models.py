from django.db import models

# Create your models here.

class MaterialCourse(models.Model):
    TIPOS_ARQUIVOS = [
        ('pdf', 'PDF'),
        ('word', 'Word'),
        ('ppt', 'PowerPoint'),
    ]
    
    title_course = models.CharField(max_length=100, verbose_name="Título")
    description_course = models.TextField(blank=True, null=True, verbose_name="Descrição")
    archive_course = models.FileField(upload_to='materiais_curso/', verbose_name="Arquivo")
    archive_course_type = models.CharField(
        max_length=5,
        choices=TIPOS_ARQUIVOS,
        verbose_name="Tipo de Arquivo"
    )
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")
    
    def __str__(self):
        return f"{self.title_course} ({self.archive_course_type})"