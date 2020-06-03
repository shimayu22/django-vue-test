from django.conf.urls import include, url
from rest_framework import routers

from stocks.views import StockViewSet, index

app_name = 'stocks'

router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'', index, name="index"),
]
