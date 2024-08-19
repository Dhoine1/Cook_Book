from django.urls import path
from .views import *

urlpatterns = [
    path('start/', start, name='start'),

    path('games/', ListOfGame.as_view()),
    path('games/<int:pk>', StoryDetail.as_view(), name="story_view"),

    path('receipts/', ListOfReceipts.as_view(), name="receipts"),
    path('receipt/<int:pk>', Receipt.as_view(), name="receipt_view"),
    path('create/', CreateReceipt.as_view(), name='receipt_create'),
    path('receipt/<int:pk>/edit/', ReceiptUpdate.as_view(), name='receipt_update'),
    path('receipt/<int:pk>/delete/', ReceiptDelete.as_view(), name='receipt_delete'),

    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
    path('comment/<int:pk>/edit/', CommentUpdate.as_view(), name='comment_update'),
    path('fact/', fact, name='fact'),
]
