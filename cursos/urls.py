from . import views
from django.urls import path, include

urlpatterns=[
    path('', views.Lista_De_Cursos, name="course_list"),
    path('listadecursos/', views.PermisoPagina.as_view(),name='course_list2'),
    path('<int:course_pk>/<int:lesson_pk>/', views.lesson_detail),
    path('<int:pk>', views.course_detail, name="course_detail"),
    
]