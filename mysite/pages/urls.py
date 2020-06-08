from django.urls import path
from . import views
from django.contrib.auth import login,logout,password_validation
from django.contrib.auth.views import (PasswordResetView,PasswordChangeView,PasswordResetDoneView,
                                       PasswordResetConfirmView,PasswordResetCompleteView)
from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.base,name='base'),
    path('about/',views.about,name='about'),
    path('base/',views.base,name='base'),
    path('index/edit/',views.edit,name='edit'),
    path('index/edit/choose/',views.choose,name='choose'),
    path('index/edit/blur/',views.blur,name='blur'),
    path('index/edit/rotate/',views.rotate,name='rotate'),
    path('index/edit/bright/',views.bright,name='bright'),
    path('index/edit/face/',views.face,name='face'),
    path('index/edit/contrast/',views.contrast,name='contrast'),
    path('index/edit/mirror/',views.mirror,name='mirror'),
    path('index/',views.index,name='index'),
    path('common/',views.common,name='common'),
    path('accounts/login/',views.home,name='home'),
    path('accounts/password_reset/',PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password_change/',PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_reset/complete',PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^accounts/password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


