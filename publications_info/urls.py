from django.urls import path
from publications_info import views

urlpatterns = [
    path("publications_infos/", views.PublicationsInfoList.as_view()),
    path("publications_infos/update/<int:pk>/", views.PublicationsInfoDetail.as_view()),
    path("publications_infos/get/<int:pk>/", views.PublicationsInfoGetDetail.as_view()),
]