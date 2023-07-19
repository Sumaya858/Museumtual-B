from django.urls import path
from .views import MuseumtualListCreate
from .views import MuseumtualDeleteView
from .views import MuseumtualUpdateView
from .views import MuseumtualRetrieveView
from .views import MuseumtualCreateView

urlpatterns = [
    path('api/museumtual/', MuseumtualListCreate.as_view()),
    path('api/museumtual/<pk>/delete', MuseumtualDeleteView.as_view()),
    path('api/museumtual/<pk>/update', MuseumtualUpdateView.as_view()),
    path('api/museumtual/<pk>/retrieve', MuseumtualRetrieveView.as_view()),
    path('api/museumtual/create', MuseumtualCreateView.as_view()),

]
