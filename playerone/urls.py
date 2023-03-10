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

# Add this once you're ready to create users
# from playeroneapi.views import register_user, check_user, CommentView, CommentReactionView, VideoGameView, ReactionView
from playeroneapi.views import register_user, check_user, VideoGameView, CommentView, ReactionView, CommentReactionView, GameGenreView, UserView, CommentGameView
# from playeroneapi.views import CommentReactionView, VideoGameView, ReactionView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'videogames', VideoGameView, 'videogames')
router.register(r'users', UserView, 'users')
router.register(r'comments', CommentView, 'comments')
router.register(r'reactions', ReactionView, 'reactions')
# router.register(r'comments', ReactionView, 'comments')
router.register(r'commentreactions', CommentReactionView, 'commentreactions')
router.register(r'gamegenres', GameGenreView, 'gamegenres')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('comment/<int:game_id>/', CommentGameView.as_view(), name='game'),
]
