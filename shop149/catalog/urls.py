from rest_framework import routers

from .views import PharmacyViewSet
from pages.views import PageViewSet


router = routers.DefaultRouter()
router.register(r'pharmacies', PharmacyViewSet)
router.register(r'pages', PageViewSet) 

urlpatterns = router.urls
