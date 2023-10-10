
from django.contrib import admin
from django.urls import path,include
from  api.views import (initiate_stk_push,payment,payment_success,)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', payment, name='payment'),
    path('initiate_stk_push/', initiate_stk_push, name='initiate_stk_push'),
    path('payment_success/', payment_success, name='payment_success'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
   

]
