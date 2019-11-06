from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.qbList, name='qbList'),
    path('add_qb/', views.add_qb, name='add_qb'),
    path('detail_qb/(?P<name>[.])', views.detail_qb, name='detail_qb'),
    path('upload_qbfile/', views.upload_qbfile, name='upload_qbfile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)