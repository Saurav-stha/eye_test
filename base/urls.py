
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name="index"),
    path('try/',views.tryin),
    path('show/',views.showImgs, name="show-imgs"),
    path("uploadImg/", views.uploadImg, name="upload-img"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

