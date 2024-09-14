from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipantViewSet, GroupViewSet, ExpenseViewSet, PaidForViewSet, AttachmentViewSet

router = DefaultRouter()
router.register(r'participants', ParticipantViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'paid-for', PaidForViewSet)
router.register(r'attachments', AttachmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]