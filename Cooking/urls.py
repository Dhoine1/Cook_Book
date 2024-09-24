from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('tuliuscookbook/', include('TuliusCookBook.urls')),
    path('countryreceipts/', include('Country.urls')),
    path('', index, name='index'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
