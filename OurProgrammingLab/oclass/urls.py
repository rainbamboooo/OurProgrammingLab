from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:lesson_id>", views.lessons, name="lessons"),
    path("runcpp", views.run_code, name="runcode"),
    path("checkmsg", views.check_msg, name="checkmsg"),
    path("newmsg", views.new_msg, name="newmsg"),
]
