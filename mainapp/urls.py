from django.urls import path
from .views import predict_tip_view,index,item_list,employee_list, add_employee, edit_employee, delete_employee,employee_duties,empLogin,empHome

urlpatterns = [
  path('/predict', predict_tip_view, name='predict_tip'),
  path('',index,name="index"),
  path('itemlist', item_list, name='item_list'),
  path('employee_list', employee_list, name='employee_list'),
    path('add/', add_employee, name='add_employee'),
    path('edit/<int:employee_id>/', edit_employee, name='edit_employee'),
    path('delete/<int:employee_id>/', delete_employee, name='delete_employee'),
     path('duties/', employee_duties, name='employee_duties'),
     path('emplogin/',empLogin,name="empLogin"),
     path("emphome/",empHome,name="emphome")
]
