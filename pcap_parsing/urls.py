from django.urls import path, include
from pcap_parsing import views

urlpatterns = [
    path('', views.PcapIndexView.as_view(), name='pcap_index'),
    path('upload/', views.PcapUploadView.as_view(), name='pcap_upload')
]