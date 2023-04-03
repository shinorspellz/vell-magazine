from django.urls import path
from articles import views

urlpatterns = [
    path("articles/", views.ArticleList.as_view()),
    path("articles/update/<int:pk>/", views.ArticleDetail.as_view()),
    path("articles/get/<int:pk>/", views.ArticleGetDetail.as_view()),
]