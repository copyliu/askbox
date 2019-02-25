"""askbox URL Configuration

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
from django.conf.urls import url
# from django.contrib import admin
from ask import views as ask_view
from django.contrib.auth.views import login, logout

urlpatterns = [
url(r'^ask/(?P<ID>.+)/post$', ask_view.postnew),
    url(r'^ask/(?P<ID>.+)/$', ask_view.default),


url(r'^admin/(?P<ID>.+)/list$', ask_view.admin_list),
url(r'^admin/(?P<ID>.+)/read$', ask_view.admin_read),
url(r'^admin/(?P<ID>.+)/del$', ask_view.admin_delete),
url(r'^admin/(?P<ID>.+)/$', ask_view.admin_page),
url(r'^login/$', login),
               url(r'^logout/$', logout, ),
               url(r'^register/$', ask_view.register),
    # url(r'^admin/', admin.site.urls),
]
