"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from playeroneapi.models import GameGenre


class GameGenreView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game_genre = GameGenre.objects.get(pk=pk)
        serializer = GameGenreSerializer(game_genre)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_genres = GameGenre.objects.all()  
        serializer = GameGenreSerializer(game_genres, many = True)
        return Response(serializer.data)
      
      # I dont think the destroy and update is needed 
      # May want to create an add remove 
      # decorator 
      
    
    # def update(self, request, pk):
    #     """Handle PUT requests for a game

    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """

    #     game = Game.objects.get(pk=pk)
    #     game.title = request.data["title"]
    #     game.maker = request.data["maker"]
    #     game.number_of_players = request.data["number_of_players"]
    #     game.skill_level = request.data["skill_level"]

    #     game_type = GameType.objects.get(pk=request.data["game_type"])
    #     game.game_type = game_type
    #     game.save()

    #     return Response(None, status=status.HTTP_204_NO_CONTENT) 
    
    # def destroy(self, request, pk):
    #     game = Game.objects.get(pk=pk)
    #     game.delete()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class GameGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = GameGenre
        fields = ('id','game_genre_name') 
        depth = 1     
