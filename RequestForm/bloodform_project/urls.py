from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from requestforms.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', transactions, name="transactions"),
    path('', home, name="home"),
    path('logout/', logout_user, name="logout")
] 
