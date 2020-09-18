from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workertable', views.workertable, name = 'workertable'),
    path('workerfullinfotable',views.workerfullinfotable, name = 'workerfullinfotable'),

    #path ('workertest',views.workertest, name = 'workertest')
]