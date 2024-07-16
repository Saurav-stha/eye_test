
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name="index"),
    path("uploadImg/", views.uploadImg, name="upload-img"),
    path("result", views.result, name="result-file"),
    path('try/',views.tryin, name="tryin"),
    path('show/',views.showImgs, name="show-imgs"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(), name='login'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

