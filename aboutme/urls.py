from django.conf.urls import include, url
from django.contrib import admin
from user_profile import views as user_profile_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'aboutme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', user_profile_views.home, name='home'),
    url(r'^login/$', user_profile_views.user_login, name='user_login'),
    url(r'^register/$', user_profile_views.user_register, name='user_register'),
    url(r'^logout/$', user_profile_views.user_logout, name='user_logout'),
    url(r'^user_profile/$', user_profile_views.user_profile, name='user_profile'),
    url(r'^show_bookings/$', user_profile_views.show_bookings, name='show_bookings')
]
