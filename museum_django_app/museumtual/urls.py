from django.urls import path
from .views import MuseumtualListCreate
from .views import MuseumtualDeleteView
from .views import MuseumtualUpdateView
from .views import MuseumtualRetrieveView
from .views import MuseumtualCreateView
from .views import BookCreateView
from .views import BookDeleteView
from .views import BookListView

from .views import MuseumtualListView

# from .views import CartCreateView
from .views import CartUpdateView
from .views import CartDeleteView
from .views import get_exhibition


from .views import MuseumListCreate
from .views import MuseumCreateView
from .views import MuseumListview
from .views import MuseumDeleteView


urlpatterns = [
    path('api/museumtual/', MuseumtualListCreate.as_view()),
    path('api/museumtual/<pk>/delete', MuseumtualDeleteView.as_view()),
    path('api/museumtual/<pk>/update', MuseumtualUpdateView.as_view()),
    path('api/museumtual/<pk>/retrieve', MuseumtualRetrieveView.as_view()),
    path('api/museumtual/create/', MuseumtualCreateView.as_view()),
    path('api/museumtual/list/', MuseumtualListView.as_view()),
    path('api/book/', BookCreateView.as_view()),
    path('api/book/<pk>/delete', BookDeleteView.as_view()),
    path('api/book/<pk>/list', BookListView.as_view()),

    # path('api/cart/', CartCreateView.as_view()),
    path('api/cart/<pk>/delete', CartDeleteView.as_view()),
    path('api/cart/<pk>/update', CartUpdateView.as_view()),
    path('api/exhibition/',get_exhibition),




    path('api/museum/', MuseumListCreate.as_view()),
    path('api/museum/create/', MuseumCreateView.as_view()),
    path('api/museum/list/', MuseumListview.as_view()),
    path('api/museum/<pk>/delete', MuseumDeleteView.as_view()),
]
