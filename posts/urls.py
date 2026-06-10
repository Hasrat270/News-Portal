#urls.py

from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
	path("", views.posts, name="posts"),
	path("posts", RedirectView.as_view(url='/', permanent=True)),
	path("posts/", RedirectView.as_view(url='/', permanent=True)),
	path("posts/create/",views.create, name="create"),
	path("posts/details/<int:id>",views.details, name="details"),
	path("posts/edit/<int:id>",views.edit, name="edit"),
	path("posts/delete/<int:id>",views.delete, name="delete"),
	path("posts/dashboard/",views.dashboard, name="dashboard"),
	path("posts/login/",views.login_view, name="login"),
	path("posts/logout/",views.logout_view, name="logout"),
	path("posts/register/",views.register_view, name="register"),
]