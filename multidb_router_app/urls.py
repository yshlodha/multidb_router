from django.conf.urls import include, url

from .views import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^product/$', ProductListView.as_view(), name='product'),
    url(r'^add-product/$', AddProductView.as_view(), name='add-product'),
    url(r'^admin-page/$', AdminPageView.as_view(), name='admin-page'),
    url(r'^admin-user-product/(?P<username>[-\w]+)/$',
        AdminUserProductView.as_view(), name='admin-user-product'),
    url(r'^admin-add-user-product/(?P<username>[-\w]+)/$',
        AdminAddUserProductView.as_view(), name='admin-add-user-product'),
   ]