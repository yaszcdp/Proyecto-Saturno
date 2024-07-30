from django.contrib import admin
from django.urls import path, include
from appcuentas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appcuentas/', include("appcuentas.urls"))
]
