from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('employees', views.EmployeeViewSet)
router.register('invoices', views.InvoiceViewSet)
router.register('products', views.ProductViewSet)
router.register('callendar', views.CallendarViewSet)
router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls