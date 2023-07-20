from django.urls import path
from .views import MuseumtualListCreate
from .views import MuseumtualDeleteView
from .views import MuseumtualUpdateView
from .views import MuseumtualRetrieveView
from .views import MuseumtualCreateView
from .views import ProfileCreateView
from .views import ProfileDeleteView
from .views import ProfileUpdateView
# from .views import CartCreateView
from .views import CartUpdateView
from .views import CartDeleteView



urlpatterns = [
    path('api/museumtual/', MuseumtualListCreate.as_view()),
    path('api/museumtual/<pk>/delete', MuseumtualDeleteView.as_view()),
    path('api/museumtual/<pk>/update', MuseumtualUpdateView.as_view()),
    path('api/museumtual/<pk>/retrieve', MuseumtualRetrieveView.as_view()),
    path('api/museumtual/create', MuseumtualCreateView.as_view()),
    path('api/profile/', ProfileCreateView.as_view()),
    path('api/profile/<pk>/delete', ProfileDeleteView.as_view()),
    path('api/profile/<pk>/update', ProfileUpdateView.as_view()),
    # path('api/cart/', CartCreateView.as_view()),
    path('api/cart/<pk>/delete', CartDeleteView.as_view()),
    path('api/cart/<pk>/update', CartUpdateView.as_view())

]
