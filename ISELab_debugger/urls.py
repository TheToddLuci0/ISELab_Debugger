"""ISELab_debugger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import base.views as base_views
from pcap_parsing import urls as pcap_urls

urlpatterns = [
    path('', base_views.IndexView.as_view(), name="site_index"),
    path('admin/', admin.site.urls),
    path('network-test/', base_views.NetworkTestView.as_view(), name="network_test"),
    path('service-test/', base_views.ServiceCheckView.as_view(), name="service_test_root"),
    path('service-test/ssh/', base_views.SSH_ServiceCheckView.as_view(), name="ssh_service_test"),
    path('service-test/http/', base_views.HTTP_ServiceCheckView.as_view(), name="http_service_test"),
    path('service-test/dns/', base_views.DNS_ServiceCheckView.as_view(), name="dns_service_test"),

    path('pcap/', include(pcap_urls))
]
