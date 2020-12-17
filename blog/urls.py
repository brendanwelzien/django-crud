from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', BlogCreateView.as_view(), name="blog_create"),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<intLpk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]