from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.qbList, name='qbList'),
    path('add_qb/', views.add_qb, name='add_qb'),
    path('your_paper/', views.your_paper, name='your_paper'),
    path('add_paper/', views.add_paper, name='add_paper'),
    path('detail_qb/<name>/', views.detail_qb, name='detail_qb'),
    path('view_ques/<id>/', views.view_ques, name='view_ques'),
    path('view_ans/<id>/', views.view_ans, name='view_ans'),
    path('upload_qbfile/<name>/', views.upload_qbfile, name='upload_qbfile'),
    # path('rename_qb/<name>/', views.rename_qb, name='rename_qb'),
    path('delete_qb/<name>/', views.delete_qb, name='delete_qb'),
    path('upload_ques_manually/<name>/', views.add_ques_manually, name='add_ques_manually'),
    path('edit_ques/<id>/', views.edit_ques, name='edit_ques'),
    path('upload_ques_by_file/<name>/', views.add_ques_by_file, name='add_ques_by_file'),
    path('paper_detail/<name>/', views.paper_detail, name='paper_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)