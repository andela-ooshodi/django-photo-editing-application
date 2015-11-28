from django.conf.urls import include, url
from django.contrib import admin
import photoapp.urls

urlpatterns = [
    url(r'^', include(photoapp.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
