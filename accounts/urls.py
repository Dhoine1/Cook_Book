from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('<int:pk>/profilecreate/', ProfileCreate.as_view(), name='profilecreate'),
    path('<int:pk>/profileupdate/', ProfileUpdate.as_view(), name='profileupdate'),
    path('users/', ListOfUser.as_view(), name="users"),
    path('user/<int:pk>', UserDetail.as_view(), name="user_view"),
    path('user/mycomments/', mycomments, name='my_comments'),
    path('user/comments_on_my_receiptes/', comments_on_my_receiptes, name="comments_on_my_receiptes"),
    path('user/mycomments_country/', mycomments_country, name="mycomments_country"),
]
