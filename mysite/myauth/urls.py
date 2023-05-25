from django.contrib.auth.views import LoginView
from django.urls import path

from .views import MyLogoutView, MainView, CalculatorView, registration, ProfileDetailView, ProfileUpdateView
from .views import downlaod_pdf, download_excel


app_name = "myauth"
urlpatterns = [
    path('register/', registration, name="register"),
    path('main/calculator/', CalculatorView.as_view(), name="calculator"),
    path('main/<int:pk>/update/', ProfileUpdateView.as_view(), name="profile_update"),
    path('main/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
    path('logout/', MyLogoutView.as_view(), name="logout"),
    path("",
         LoginView.as_view(
             template_name="myauth/login.html",
             redirect_authenticated_user=True,

         ),
         name="login"),
    path('main/', MainView.as_view(), name="main"),
    path('downlad_pdf', downlaod_pdf, name="downlad_pdf"),
    path('download_excel', download_excel, name="download_excel"),
]
