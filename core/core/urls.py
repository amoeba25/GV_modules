from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onboarding/', include('cust_onboard.urls')),  # customer onboarding url 
    
]
