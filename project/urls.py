# from django.contrib import admin
# from django.urls import path, include 
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('users.urls')),
#     path('schema/', SpectacularAPIView.as_view(), name='schema'),
#     path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#     path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),
# # <<<<<<< HEAD
    
# # =======
#     path('auth/', include('googleauth.urls')),
#     path('accounts/', include('allauth.urls')),
# #>>>>>>> googleauth
# ]
from django.contrib import admin
from django.urls import path, include 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),
    path('auth/', include('googleauth.urls')),  
    path('accounts/', include('allauth.urls')),  
    path('products/', include('products.urls')),
    path('contacts/', include('contacts.urls')),
    path('basket/', include('basket.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

