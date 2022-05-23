from django.urls import path
from .import views

urlpatterns=[
    path('',views.AddStudent,name='AddStudent'),
    path('Stud_Reg',views.Stud_Reg,name='Stud_Reg'),
    path('show_stud',views.show_stud,name='show_stud'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('delete_students/<int:pk>',views.delete_students,name='delete_students'),
    path('student_details/<int:pk>',views.student_details,name='student_details')
]
