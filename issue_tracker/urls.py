"""
URL configuration for issue_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from comments.views import comments_view
from projects.views import projects_view
from users.views import login_view, logout_view
from tickets.views import redirect_to_home, tickets_view, ticket_edit_view
from media.views import images_view

urlpatterns = [
    path("login", login_view, name="login_view"),
    path("logout", logout_view, name="logout_view"),
    path("tickets", tickets_view, name="tickets_view"),
    path("projects", projects_view, name="projects_view"),
    path("ticket/<int:ticket_id>/edit/view", ticket_edit_view, name="ticket_edit_view"),
    path("comments", comments_view, name="comments_view"),
    path("images", images_view, name="images_view"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path("", redirect_to_home, name="redirect_to_home")]
