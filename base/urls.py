from unicodedata import name
from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('blog-create/', views.PostCreateView.as_view(), name="blog-create"),
    path('blog-detail/<int:pk>', views.PostDetailView.as_view(), name="blog-detail"),
    path('blog-update/<int:pk>', views.PostUpdateView.as_view(), name="blog-update"),
    path('blog-delete/<int:pk>', views.PostDeleteView, name="blog-delete"),
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category-detail/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    path('like/<int:pk>', views.LikeBlog, name='like-blog'),
    path('dislike/<int:pk>', views.DisLikeBlog, name='dislike-blog'),
    path('delete-comment/<int:pk>', views.DeleteComment, name='delete-comment'),
    path('comment/<int:pk>', views.AddComment, name='add-comment'),
    path('comment-update/<int:pk>', views.UpdateComment.as_view(), name='update-comment'),
    path('unlike/<int:pk>', views.RemoveLike, name="remove-like"),
    path('remove-dislike/<int:pk>', views.RemoveDisLike, name="remove-dislike"),
]
