"""smart URL Configuration

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
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('projects/')),
    url(r'^api/', include('core.urls.api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('core.urls.projects', namespace='projects')),
]

# Don't show API docs in production
if settings.DEBUG:
    swagger_docs_view = get_swagger_view(title='SMART')

    urlpatterns.append(url(r'^docs/', swagger_docs_view))
