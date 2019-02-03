from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    DocView,
    DocDetailView,
)

urlpatterns = [
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^doc/$', DocView.as_view(), name='Doc_view'),
    url(r'doc/(?P<doc_id>\d+)/', DocDetailView.as_view(), name='Doc_detail'),
]