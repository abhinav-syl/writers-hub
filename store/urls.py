from django.urls import include

from django.urls import path, include
from .views import (
    ArticleApiView,
    ArticleSpecificApiView,
    AuthorApiView,
    AuthorSpecificApiView,
    index,
    pages,)

urlpatterns = [
    path('index/', index),
    path('pages/<str:title>', pages),
    path('api/authors', AuthorApiView.as_view(), name='authors'),
    path('api/articles', ArticleApiView.as_view(), name='articles'),
    path('api/articles/<str:title>', ArticleSpecificApiView.as_view(), name='articles_specific'),
    path('api/authors/<str:first_name>', AuthorSpecificApiView.as_view(), name='author_specific'),
]
