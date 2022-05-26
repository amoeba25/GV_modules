import imp
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onboarding/', include('cust_onboard.urls')),  # customer onboarding url 
    path('leave/', include('leave_manage.urls'))
    # path('detection/', include('video_detect.urls')), 
    # path('production/', include('production.urls')), 
] + static(settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)
