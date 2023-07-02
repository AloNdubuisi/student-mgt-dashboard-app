from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_student', views.add_student,  name = 'add_student'),
    path('delete_student/<int:regnum>', views.delete_student,  name = 'delete_student'),    
    path('update_student/<int:regnum>', views.update_student,  name = 'update_student'),
    path('edit_update_student/<int:regnum>',views.edit_update_student, name='edit_update_student')       
]
