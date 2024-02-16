from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from HW.views import login_, StudentAPIView, HWAPIModelViewSet, HWParamsAPIView, main_


router = routers.SimpleRouter()
router.register(r'HW', HWAPIModelViewSet)
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/mainHW/', HWParamsAPIView.as_view()),
    path('api/v1/HW/answer/<int:pk>', StudentAPIView.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/login-page/', login_, name='hw'),
    path('api/v1/main/', main_, name='main')
]
