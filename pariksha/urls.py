from django.conf.urls import url
from django.contrib import admin
from .prak import urls
from .stud import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
