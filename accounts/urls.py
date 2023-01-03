from django.contrib import admin
from django.urls import path, include
from .views import signup,profile#,transaction

urlpatterns = [
    path('admin/', admin.site.urls),
   # path(r'^admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
  #  path('transaction-request/', transaction, name='transaction-request'),
   #path('test/', test1, name='test1'),
    path('', include('django.contrib.auth.urls')),
]