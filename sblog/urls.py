from django.conf.urls import *
from sblog.views import chapter

urlpatterns = patterns('', url(r'^$', chapter), )
