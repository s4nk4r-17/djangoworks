"""
URL configuration for djcalculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import AdditionView
from operation.views import SubtractionView
from operation.views import MultiplicationView
from operation import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path("addition/",AdditionView.as_view()),

    path("subtract/",SubtractionView.as_view()),

    path("multi/",MultiplicationView.as_view()),

    path('reg/',views.SignUpView.as_view()),

    path("vehicle/",views.VehicleAddView.as_view()),

    path("bmr/",views.BmrView.as_view()),

    path("appoint/",views.AppointmentView.as_view()),

    path("bmi/",views.BmiView.as_view()),

    path("milage/",views.MilageView.as_view()),

    path("emi/",views.EmiView.as_view()),

    path("calorie/",views.CalorieView.as_view()),

]
