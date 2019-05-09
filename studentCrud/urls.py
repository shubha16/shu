from django.urls import path

from studentCrud import views


app_name = 'studentCrud'

urlpatterns = [
    path('', views.login, name='login'),
    path('success', views.success, name='success'),
    path('add_student', views.add_student, name='add_student'),
    path('student_edit/<int:pk>',views.student_edit, name='student_edit'),
    path('student_delete/<int:pk>',views.student_delete, name='student_delete'),
    path('logout', views.logout, name='logout'),
]