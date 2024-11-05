from django.urls import path
from . import views 
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns (test)
#urlpatterns+=staticfiles_urlpatterns() (test)
urlpatterns = [
    path('', views.stock_form, name='stock_form'),

]

