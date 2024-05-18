from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
    # crud operations

    # create record
    path("create_record", views.create_record, name="create_record"),
    # view record
    path("view_record/<str:pk>", views.view_record, name="view_record"),
    # delete record
    path("delete_record/<str:pk>", views.delete_record, name="delete_record"),
    # update record
    path("update_record/<str:pk>", views.update_record, name="update_record"),
]

