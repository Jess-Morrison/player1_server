"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from playeroneapi.models import VideoGame, User, GameGenre


class VideoGameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        video_game = VideoGame.objects.get(pk=pk)
        serializer = VideoGameSerializer(video_game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        video_games = VideoGame.objects.all()
  
        serializer = VideoGameSerializer(video_games, many = True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = User.objects.get(pk=request.data["userId"])
        # why did I have to change this to uid?
        # This should probably be pk instead of uid, you are trying to grab the pk
        game_genre = GameGenre.objects.get(pk=request.data["gameGenre"])

        video_game = VideoGame.objects.create(
        game_title=request.data["gameTitle"],
        purchase_location=request.data["purchaseLocation"],
        game_format=request.data["gameFormat"],
        description=request.data["description"],
        image_url=request.data["imageUrl"],
        # game_genre=request.data["gameGenre"],
        user=user,
        game_genre=game_genre
        )
        serializer = VideoGameSerializer(video_game)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        video_game = VideoGame.objects.get(pk=pk)
        video_game.game_title = request.data["game_title"]
        video_game.purchase_location = request.data["purchase_location"]
        video_game.game_format = request.data["game_format"]
        video_game.description = request.data["description"]
        video_game.image_url = request.data["image_url"]

        # So if the primary key from game genre matches the game_genre
        # in video games object
        game_genre = GameGenre.objects.get(pk=request.data["game_genre"])
        video_game.game_genre = game_genre
        video_game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT) 
    
    def destroy(self, request, pk):
        video_game = VideoGame.objects.get(pk=pk)
        video_game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class VideoGameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = VideoGame
        fields = ('id', 'user', 'game_genre', 'game_title', 'purchase_location', 'game_format', 'description', 'image_url') 
        depth = 1     
