from django.urls import path
from .views import *

urlpatterns = [
    path('start/', start, name='country_start'),
    path('countries/', ListOfCountries.as_view()),
    path('country/<int:pk>', CountryDetail.as_view(), name="country_view"),
    path('receipt/<int:pk>', Receipt.as_view(), name="receipt_country_view"),
    path('receipts/', ListOfReceipts.as_view(), name="receipts_country"),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_country_delete'),
    path('comment/<int:pk>/edit/', CommentUpdate.as_view(), name='comment_country_update'),
]
