from django.conf.urls import url
from django.contrib import admin
from home import views as home_views

urlpatterns = [

    # prosignup.com/
    url(r'^$', home_views.index, name="index"),

    # prosignup.com/admin/
    url(r'^admin/', admin.site.urls),

    # prosignup.com/657/
    url(r'^(?P<user_id>[0-9]+)/$', home_views.show , name="show"),

    # prosignup/lksdafskdflasfdl
    url(r'^(?P<user_link>[a-z]+)/$', home_views.do_it, name="do_it"),

]
