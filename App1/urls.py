from django.urls import path, include
from . import views
urlpatterns = [
    path("login/", views.login_view, name="login"),
    # path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path('list/', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='create'),  # וודא שהשם הוא create כפי שמופיע ב-html
    path('task/update/<int:id>/', views.task_update, name='update'),
    path('task/delete/<int:id>/', views.task_delete, name='delete'),

    # הנתיבים החדשים:
    path('task/claim/<int:id>/', views.task_claim, name='claim'),
    path('task/complete/<int:id>/', views.task_complete, name='complete'),
    path('select-role-and-team/', views.select_role_and_team, name='select_role_and_team'),

    # path('enroll/<str:tz>/', views.student_enroll, name='student_enroll'),

]