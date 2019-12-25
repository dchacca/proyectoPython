from django.urls import path
from .views import HomePageView, ItemCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="blog"),
    path("crear-post", ItemCreateView.as_view(), name="add_blog_item")
]
