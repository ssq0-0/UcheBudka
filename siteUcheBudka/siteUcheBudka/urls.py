from django.contrib import admin
from django.urls import path
from HW.views import HWAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/HW/', HWAPIView.as_view()),
    path('api/v1/HW/<int:pk>/', HWAPIView.as_view()),
]
