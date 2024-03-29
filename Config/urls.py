"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from Users.views import LoginView, SignupView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('accounts/login/', LoginView.as_view(), name="account_login"),
    path('accounts/signup/', SignupView.as_view(), name="account_signup"),
    path('accounts/', include('allauth.urls')),
] + i18n_patterns(
    path('admin/', admin.site.urls),
    path('apis/', include('APIs.urls')),
    path('', include('Base.urls')),
    path('', include('Posts.urls')),
    path('user/', include('Users.urls')),
    path('', include('Articles.urls')),
    path('', include('Comments.urls')),
    # path('register/', include('django.contrib.auth.urls')),

) + static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL, document_root = settings.STATIC_ROOT
)
