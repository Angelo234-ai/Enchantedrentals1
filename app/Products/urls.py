from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('Products/<str:category>', views.Products.as_view(), name="products"),
    path('Rentalpolicy/', views.Rentalpolicy.as_view(), name="policy"),
    path('Contact/', views.Contact, name="contact")
]
