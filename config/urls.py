from django.conf.urls import include, url
from stocks.urls import urlpatterns as qiitalist_url

urlpattern = [
    url(r'^qiita/', include(qiitalist_url)),
]
