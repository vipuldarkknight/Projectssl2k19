from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.qbList, name='qbList'),
    path('add_qb/', views.add_qb, name='add_qb'),
    path('detail_qb/<name>/', views.detail_qb, name='detail_qb'),
    path('upload_qbfile/<name>/', views.upload_qbfile, name='upload_qbfile'),
    path('delete_qb/<name>/', views.delete_qb, name='delete_qb'),
    path('upload_ques_manually/<name>/', views.add_ques_manually, name='add_ques_manually'),
    path('edit_ques/<id>/', views.edit_ques, name='edit_ques'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)