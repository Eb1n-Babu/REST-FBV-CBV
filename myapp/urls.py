from django.urls import path
from .views import books_list, book_detail, book_create, book_update, book_delete, AutherViewSet , StudentViewSet


urlpatterns = [
    path("", books_list),
    path("<int:pk>/", book_detail),
    path("create/", book_create),
    path("<int:pk>/update", book_update),
    path("<int:pk>/delete", book_delete),
    path('author/', AutherViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('author/<int:pk>/', AutherViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('student/<int:pk>',StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

