from django.urls import path
from roles import views

urlpatterns = [
    path("roles/", views.RoleList.as_view()),
    path("roles/update/<int:pk>/", views.RoleDetail.as_view()),
    path("roles/get/<int:pk>/", views.RoleUserDetail.as_view()),
]