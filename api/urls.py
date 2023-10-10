from   django.urls import path
from .views import LNMCallbackUrlAPIView,C2BConfirmationAPIView,C2BValidationAPIView

urlpatterns=[
    path('lipanampesa/',LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
    path("c2b-validation/", C2BValidationAPIView.as_view(), name="c2b-validation"),
    path("c2b-confirmation/", C2BConfirmationAPIView.as_view(), name="c2b-confirmation"),
]