from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^\.well-known/appspecific/com\.chrome\.devtools\.json$', lambda request: JsonResponse({})),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)