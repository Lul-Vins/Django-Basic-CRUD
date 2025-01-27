from django.urls import path
from .views import ArticleListView, ArticlePerID, ArticleCreateView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticlePerID.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('delete/<int:id>/', ArticleDeleteView.as_view(), name='article-delete'),
    path('update/<int:id>/', ArticleUpdateView.as_view(), name='article-updaute'),
]