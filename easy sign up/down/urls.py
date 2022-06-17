from django.contrib import admin
from django.urls import path, include
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', Registration.as_view(), name='signup'),
    path('', include('website.urls')),
]
