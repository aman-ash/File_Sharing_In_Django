from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Upload import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('file/', views.file_list, name='file'),
    path('file/upload/', views.upload_file, name='upload_file'),
    # path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
