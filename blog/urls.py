from django.urls import path
from . import views
urlpatterns = [
    path("", views.StartPageView.as_view(), name="starting_page"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(),
         name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]
