from django.urls import path
from .views import *

urlpatterns = [
    path('student/', student_view_api),
    path('student/<int:id>/', student_update_api),
]