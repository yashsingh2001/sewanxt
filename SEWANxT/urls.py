"""
URL configuration for SEWANxT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from SEWANxT import views
from .views import signup
from django.urls import path, include


urlpatterns = [
      
      
      path('admin/', admin.site.urls),
      path('', views.home),
      path('thankssignuppage/', views.thankssignuppage),
      path('login/', views.login),
      path('login/recipt', views.recipt),


      path('login/trainingppt', views.trainingppt),
      path('login/trainingppt/certificate', views.certificate),

    


      path('login/trainingppt/certificate/discount', views.generate_qr),
      path('login/help', views.help),
      path('login/insurancedetails/', views.insurancedetails),
      path('login/policydetails/', views.policydetails),

   path('login/policydetails/planselection', views.planselection),

      path('login/policydetails/planselection/insurancedetails', views.insurancedetails),
      path('login/noncrop/', views.noncrop),
         path('login/Crop', views.Crop), 
 
      path('login/noncrop/personaldetails', views.personaldetails),
      path('login/noncrop/personaldetails/insurancedetails', views.insurancedetails),
      path('login/noncrop/policydetails/', views.policydetails),
      path('login/noncrop/personaldetails/policydetails/', views.policydetails),
      path('savelogin/', views.savelogin,name="savelogin"),
       path('savenoncrop', views.savenoncrop, name='savenoncrop'),
       path('signup/', views.signup, name='signup'),
        path('thank-you/', views.thankssignuppage, name='thank_you_signup'),

    #   path('personaldetails/', views.personal_details, name='personaldetails'),
   
    # path('next/', views.personal_details, name='next'), 
    #   path('admin/', admin.site.urls),

    #  path('personaldetails/', include('personaldetails.urls')),
    #    path('personaldetails/', views.personal_details, name='personaldetails'),



]


