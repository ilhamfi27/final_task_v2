from django.urls import path
from . import views

app_name = 'predicts'
urlpatterns = [
    path('', views.index, name='index'),
    path('predictor/', views.predictor, name='predictor'),
    path('mapping/', views.mapping, name='mapping'),
    path('prediction_result/<int:prediction_id>/', views.prediction_result, name='prediction_result'),
    path('api/fs_last_result/<slug:fs_algorithm>/', views.fs_last_result, name='fs_last_result'),
]
