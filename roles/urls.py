from django.urls import path
from roles import views

urlpatterns = [
    path("roles/", views.RoleList.as_view()),
    path("rolesupdate/<int:pk>/", views.RoleDetail.as_view()),
    path("roleget/<int:pk>/", views.RoleUserDetail.as_view()),
]
