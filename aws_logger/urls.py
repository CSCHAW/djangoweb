from django.contrib import admin
from django.urls import path
from aws_logger.views import log, view_log

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', log),
    path('view_log/', view_log),
]
