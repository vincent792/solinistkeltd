from   django.urls import path
from .views import LNMCallbackUrlAPIView

urlpatterns=[
    path('lipanampesa/',LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
]