from django.urls import path
from .views import SignUp, ProfileCreate, ProfileUpdate, ListOfUser, UserDetail

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('<int:pk>/profilecreate/', ProfileCreate.as_view(), name='profilecreate'),
    path('<int:pk>/profileupdate/', ProfileUpdate.as_view(), name='profileupdate'),
    path('users/', ListOfUser.as_view(), name="users"),
    path('user/<int:pk>', UserDetail.as_view(), name="user_view"),
]
