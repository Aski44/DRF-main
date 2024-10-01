from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserCreateAPIView, UserListAPIView, PaymentsCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payments", PaymentsViewSet)

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("", UserListAPIView.as_view(), name="users_list"),
    path("<int:pk>/", UserListAPIView.as_view(), name="user_detail"),
    path("<int:pk>/update/", UserListAPIView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserListAPIView.as_view(), name="user_delete"),
    path("paymentstripe/", PaymentsCreateAPIView.as_view(), name="paymentstripe"),
]

urlpatterns += router.urls
