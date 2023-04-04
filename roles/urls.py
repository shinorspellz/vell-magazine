from django.urls import path
from roles import views

urlpatterns = [
    path("roles/", views.RoleList.as_view()),
<<<<<<< HEAD
    path("roles/update/<int:pk>/", views.RoleDetail.as_view()),
    path("roles/get/<int:pk>/", views.RoleUserDetail.as_view()),
]
=======
    path("rolesupdate/<int:pk>/", views.RoleDetail.as_view()),
    path("roleget/<int:pk>/", views.RoleUserDetail.as_view()),
]
>>>>>>> 5f668f651ff54ac0e34ae487d5b780b70f7ee1c8
