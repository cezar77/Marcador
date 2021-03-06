"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('marcador_api.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('marcador.urls')),
    url(
        r'^login/$',
        LoginView.as_view(template_name='login.html'),
        name='mysite_login'
    ),
    url(
        r'^logout/$',
        LogoutView.as_view(next_page=reverse_lazy('bookmark-list')),
        name='mysite_logout'
    ),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns