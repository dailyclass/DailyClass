from django.db import models

# Create your models here.
#nombre de clase primera letra mayuscula
class Curso(models.Model):
    datecreate = models.DateTimeField(auto_now_add=True)
    tittle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title    

