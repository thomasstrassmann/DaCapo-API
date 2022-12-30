from bookmarks import views
from django.urls import path

urlpatterns = [
    path('bookmarks/', views.BookmarkList.as_view()),
    path('bookmarks/<int:pk>/', views.BookmarkDetail.as_view()),
]
