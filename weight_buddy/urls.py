from django.urls import path
from . import views

urlpatterns = [    
    
    path('', views.workout_list, name='workout_list'),
    path('training/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('training/new', views.training_new, name='training_new'),
    path('training/<int:pk>/edit/', views.training_edit, name='training_edit'),

    path('exercises/', views.exercise_list , name='exercise_list'),
    path('exercises/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercises/new', views.exercise_new, name='exercise_new'),
    path('exercises/<int:pk>/edit/', views.exercise_edit, name='exercise_edit'),

]