from rest_framework import routers


from .viewsets import CursoViewSet 


router = routers.SimpleRouter()
router.register('cursos', CursoViewSet)

urlpatterns = router.urls