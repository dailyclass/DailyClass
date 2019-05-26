from django.contrib import admin
from .models import Perfiles, PerfilesUsuario
# Register your models here.

#class LessonInline(admin.StackedInline):
class PerfilUSuarioInline(admin.TabularInline):
    model = PerfilesUsuario


class CursoAdmin(admin.ModelAdmin):
    inlines = [PerfilUSuarioInline]



admin.site.register(Perfiles)
admin.site.register(PerfilesUsuario)

