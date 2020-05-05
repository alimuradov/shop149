
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from catalog.views import PillList, data_fill, search
from catalog.cron import import_dbf_job


urlpatterns = [
    url(r'^api/v1/', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('summernote/', include('django_summernote.urls')),
    url(r'^pills/$', PillList.as_view()),
    url(r'^search/$', search),
    url(r'^api/v1/datafill/$', data_fill),
    # url(r'^import_dbf/$', import_dbf_job),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))

    ] + urlpatterns    
