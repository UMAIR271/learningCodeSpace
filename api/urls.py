from django.urls import path
from api.views import *

urlpatterns = [
    path('server/', server.as_view()),
]