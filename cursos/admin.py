from django.contrib import admin
from .models import Curso, Lesson
# Register your models here.


#class LessonInline(admin.StackedInline):
class LessonInline(admin.TabularInline):
    model = Lesson


class CursoAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


admin.site.register(Curso, CursoAdmin)
#admin.site.register(Lesson)