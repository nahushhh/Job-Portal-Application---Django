from django.contrib import admin
from django.urls import path, include
from JobPortalApp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('company-register', views.company_register, name="company_register"),
    path('company-login', views.company_login, name="company_login"),
    path('user-login', views.user_login, name="user_login"),
    path('user-register', views.user_register, name="user_register"),
    path("post-job", views.post_job, name="post_job"),
    path("all-jobs", views.all_jobs, name="all_jobs"),
    path("display-all-jobs", views.display_all_jobs, name="display_all_jobs"),
]