from . import views
from django.urls import path
from .views import delete_student
urlpatterns = [
    path("",views.FV,name="FV"),
    path("sem3",views.sem3,name="sem3"),
    path("sem5",views.sem5,name="sem5"),
    path("sem7",views.sem7,name="sem7"),
    path("faculty_view", views.faculty_view, name="faculty_view"),
    path("add_manually", views.add_manually, name="add_manually"),
    path('delete_student/<str:roll>/', delete_student, name='delete_student')
]
