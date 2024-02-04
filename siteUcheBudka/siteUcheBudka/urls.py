from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from HW.views import HWAPIView, login_, test_, HWAPIUpdateView, HWAPIDestroyView, StudentAPIView, HWAPIPostView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/HW/', HWAPIGetView.as_view()),
    path('api/v1/HW/<int:pk>/', HWAPIGetView.as_view()),
    path('api/v1/HW/edit/<int:pk>/', HWAPIUpdateView.as_view()),
    path('api/v1/HW/create/', HWAPIPostView.as_view()),
    path('api/v1/HW/delete/<int:pk>/', HWAPIDestroyView.as_view()),
    path('api/v1/HW/answer/<int:pk>/', StudentAPIView.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/login-page/', login_, name='hw'),
    path('api/v1/test/', test_, name='test')
]
