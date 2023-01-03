from django.urls import path
from wanted import views

urlpatterns = [
    path('wanted/', views.WantedList.as_view()),
    path('wanted/<int:pk>/', views.WantedDetail.as_view())
]
