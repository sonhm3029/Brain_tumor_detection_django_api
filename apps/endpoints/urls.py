from django.urls import include, re_path,path
from rest_framework.routers import DefaultRouter
from apps.endpoints.views import PredictView

router = DefaultRouter(trailing_slash=False)
# router.register(r"brain-tumor-prediction",PredictView,basename='brain-tumor-prediction')


urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    path("brain-tumor/prediction", PredictView.as_view())
]