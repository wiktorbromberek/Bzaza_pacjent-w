from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home ,name="home"),
    path('user/', views.userPage, name="user"),

    path('konto/',views.ustawieniaKonta, name="konto"),

    # path('lekarzs', views.lekarzs, name="lekarzs" ),
    path('pacjent/<str:pk>/', views.pacjent, name="pacjent" ),

    path('create_wizyta/<str:pk>/',views.createWizyta, name="create_wizyta"),
    path('update_wizyta/<str:pk>/',views.updateWizyta, name="update_wizyta"),
    path('delete_wizyta/<str:pk>/',views.deleteWizyta, name="delete_wizyta"),

]
