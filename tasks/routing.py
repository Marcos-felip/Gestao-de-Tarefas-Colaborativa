from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/tasks/(?P<room_name>\d+)/$', consumers.CommentConsumer.as_asgi()),
]
