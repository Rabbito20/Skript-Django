from django.urls import path

from .views import HomeView, EntryView, CreateBlogView

urlpatterns = [
    path('', HomeView.as_view(), name='apk-home'),
    path('article/<int:pk>/', EntryView.as_view(), name='article-detail'),
    path('create_article/', CreateBlogView.as_view(success_url='/'), name='create_article'),

    #path('', views.index, name='index'),
    #path('articles/', views.articles, name='articles'),
    #path('article/<int:id>', views.articles, name='article'),
    #path('edit/<int:id>', views.edit, name='edit'),
    #path('new/', views.new, name='new'),
]