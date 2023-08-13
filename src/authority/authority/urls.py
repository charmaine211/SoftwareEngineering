from django.contrib import admin
from django.urls import include, path, re_path
from ou.views import IndexView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    path('ou/', include('ou.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
