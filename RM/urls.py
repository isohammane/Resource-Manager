from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "RM Admin"
admin.site.site_title = "RM Admin Portal"
admin.site.index_title = "Welcome to Resorse Manager"
