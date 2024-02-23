from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from HW.views import login_, StudentAPIView, HWAPIModelViewSet, HWParamsFroStudentAPIView, TeacherMarkAPIViewSet, UserRegistrationAPIView, DiaryAPIView, main_, HWPage_, Diary_


router = routers.SimpleRouter()
router.register(r'HW', HWAPIModelViewSet)
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/registrations/', UserRegistrationAPIView.as_view()),
    path('api/v1/mainHW/', HWParamsFroStudentAPIView.as_view()),
    path('api/v1/SetMarkHW/', TeacherMarkAPIViewSet.as_view()),
    path('api/v1/HW/answer/<int:pk>/', StudentAPIView.as_view()),
    path('api/v1/my_hw/', DiaryAPIView.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/login-page/', login_, name='hw'),
    path('api/v1/main/', main_, name='main'),
    path('api/v1/HWPage/', HWPage_, name='HWPage'),
    path('api/v1/Diary/', Diary_, name='diary')
]
