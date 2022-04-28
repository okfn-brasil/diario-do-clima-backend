from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/plans/', include('plans.urls')),
    path('api/subscriptions/', include('subscriptions.urls')),
    path('api/billing/', include('billing.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
