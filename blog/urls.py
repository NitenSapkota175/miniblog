from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('about/',views.About,name="About"),
    path('contact/',views.Contact,name="Contact"),
    path('dashboard/',views.Dashboard,name="Dashboard"),
    path('login/',views.UserLogin,name="Login"),
    path('signup/',views.UserSignup,name="Signup"),
    path('logout/',views.UserLogout,name="Logout"),
    path('addpost/',views.AddPost,name="AddPost"),
    path('updatepost<int:pk>/',views.UpdatePost,name="UpdatePost"),
    path('deletepost<int:pk>/',views.DeletePost,name="DeletePost")

]
