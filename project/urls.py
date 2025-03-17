from django.urls import path
from project.views import csrf_token_view, post_view

urlpatterns = [
    path('csrf/', csrf_token_view, name='csrf_token'),
    path('post/', post_view, name='post'),
]
