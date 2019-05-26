from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Curso, Lesson

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

'''
# Create your views here.
def Lista_De_Cursos(request):
    course=Curso.objects.all()
    Response = ', '.join([str(courses)for courses in course])
    return HttpResponse(Response)
'''

# Create your views here.
def Lista_De_Cursos(request):
    curso=Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': curso})

@login_required
def course_detail(request, pk):
    #curso = Curso.objects.get(pk=pk)
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/course_detail.html', {'cursos':curso})

def lesson_detail(request, course_pk, lesson_pk):
    lesson = get_object_or_404(Lesson, curso_id=course_pk, pk=lesson_pk)
    return render(request, 'cursos/lesson_detail.html', {'lesson':lesson})


class PermisoPagina(LoginRequiredMixin, TemplateView):
    template_name = 'cursos/lista_cursos.html'