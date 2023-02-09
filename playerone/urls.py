"""playerone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path
# Add this once you're ready to create users
# from playeroneapi.views import register_user, check_user, CommentView, CommentReactionView, VideoGameView, ReactionView
from playeroneapi.views import CommentReactionView, VideoGameView, ReactionView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'videogames', VideoGameView, 'videogame')
router.register(r'reactions', ReactionView, 'reaction')
router.register(r'comments', ReactionView, 'comment')
router.register(r'commentreactions', CommentReactionView, 'commentreaction')

urlpatterns = [
    path('admin/', admin.site.urls),
]
