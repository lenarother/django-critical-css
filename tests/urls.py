try:
    from django.urls import include, url
except ImportError:
    from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('cms.urls')),
]
