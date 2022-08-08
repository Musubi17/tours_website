from django.contrib import admin
from django.urls import path, include
from tours.views import page_not_found
# use "include" to make the app be more independent of the project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),
]

handler404 = page_not_found
