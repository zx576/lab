"""lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'recite/', include('recite.urls', namespace='recite', app_name='recite')),
    url(r'tools/', include('tools.urls', namespace='tools', app_name='tools')),
    url(r'rhyme/', include('rhyme.urls', namespace='rhyme', app_name='rhyme')),
    url(r'scan/', include('mycode.urls', namespace='mycode', app_name='mycode')),
    url(r'proxy/', include('myproxy.urls', namespace='myproxy', app_name='myproxy')),
    url(r'movie/', include('movie.urls', namespace='movie', app_name='movie')),
    url(r'', include('labpage.urls',namespace='lab',app_name='labpage'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
