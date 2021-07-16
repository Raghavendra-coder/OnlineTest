from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login_option/", views.login_option, name="login_option"),
    path("login_page/", views.login_page, name="login_page"),
    path("signup/", views.signup_page, name="signup_page"),
    path("admin_homepage/", views.admin_homepage, name="admin_homepage"),
    path("cong/", views.cong, name="cong"),
    path("schedule_test/", views.schedule_test, name="schedule_test"),
    path("test_page/", views.test_page, name="test_page"),
    path("delete_test/<pk>", views.delete_test, name="delete_test"),
    path("start_test/<pk>", views.start_test, name="start_test"),
    path("pause_test/<pk>", views.pause_test, name="pause_test"),
    path("user_homepage/", views.user_homepage, name="user_homepage"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("exam/<pk>", views.exam, name="exam"),
    path("complete/", views.complete, name="complete"),
    path("report/<pk>", views.report, name="report"),
    path("answer/<pk>", views.answer, name="answer"),
]