from rest_framework.routers import DefaultRouter
from .views import ZoneViewSet, VisitorsViewSet

router = DefaultRouter()

router.register('zones',ZoneViewSet,basename='zone')
router.register('visitors',VisitorsViewSet,basename='visitor')

urlpatterns = router.urls
