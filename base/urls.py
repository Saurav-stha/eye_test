
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name="index"),
    path("uploadImg/", views.uploadImg, name="upload-img"),
    path("result", views.result, name="result-file"),
    path('try/',views.tryin, name="tryin"),
    path('show/',views.showImgs, name="show-imgs"),
    path('signup/', views.signup, name="signup"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

