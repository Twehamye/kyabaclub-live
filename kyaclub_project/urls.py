from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kyaclub_app.urls')),
]

# config Admin Page
admin.site.site_header = "KYABASHENYI CLUB ADMIN PANEL"
admin.site.site_title = "KYABASHENYI CLUB WEBSITE"
admin.site.index_title = "Welcome To The Administration Area" 