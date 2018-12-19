from django.conf.urls import url, include
from rest_framework import routers
from customer import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^users/', views.UserViewSet.as_view(),name='user'),
    url(r'^customer/$', views.CustomerListView.as_view(),name='customer-list'),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerDetailView.as_view(),name='customer-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]