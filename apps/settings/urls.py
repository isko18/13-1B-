from rest_framework.routers import DefaultRouter

from apps.settings.views import SettingAPI

router = DefaultRouter()
router.register('setting', SettingAPI, "api_setting")

urlpatterns = router.urls