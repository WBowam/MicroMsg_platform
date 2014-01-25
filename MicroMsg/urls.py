from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MicroMsg.views.home', name='home'),
    # url(r'^MicroMsg/', include('MicroMsg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

##added by Tulpar for MicroMsg platform,2014/01/14
urlpatterns += patterns('',
    ##for weixin1,
    url(r'^weixin1$','app.weixin1.views.main',name='weixin1'),
)