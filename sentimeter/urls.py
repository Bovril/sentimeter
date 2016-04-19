# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files, display_meta, search, feedback_thanks
from rest_framework import routers
from sentimeter.apps.sent_api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^meta$', display_meta, name='meta'),
    url(r'^search/$', search, name='search'),
    url(r'^success$', feedback_thanks, name='success'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/$', include('sentimeter.apps.sent_app.urls')),
)
