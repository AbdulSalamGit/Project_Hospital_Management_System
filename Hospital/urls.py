from django.contrib import admin
from django.urls import path
from app.views import About, Nav,dashboard, home,Contact, user_login_view, logout_admin
from app.views import view_doctor , add_doctor, delete_doctor 
from app.views import view_patient, delete_patient, add_patient
from app.views import view_appointment, add_appointment, delete_appointment

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', About, name='about'),

    path('admin_login/', user_login_view, name='login'),  # Updated view name here
    path('logout/', logout_admin, name='logout'),

    path('dashboard/', dashboard, name='dashboard'),
    path('Nav/', Nav, name='Nav'),
    path('contact/', Contact, name='contact'),


    path('view_doctor/', view_doctor, name='view_doctor'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('delete_doctor/<int:pid>/', delete_doctor, name='delete_doctor'),

    path('view_patient/', view_patient, name='view_patient'),
    path('add_patient/', add_patient, name='add_patient'),
    path('delete_patient/<int:pid>/', delete_patient, name='delete_patient'),

    path('view_appointment/', view_appointment, name='view_appointment'),
    path('add_appointment/', add_appointment, name='add_appointment'),
    path('delete_appointment/<int:pid>/', delete_appointment, name='delete_appointment'),

   

]
