from rating import views
from django.urls import path

urlpatterns = [
    path('rating/', views.RatingList.as_view()),
    path('rating/<int:pk>/', views.RatingDetail.as_view()),
]
