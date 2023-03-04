"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from playeroneapi.models import Reaction, CommentReaction


class ReactionView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        reaction = Reaction.objects.get(pk=pk)
        serializer = ReactionSerializer(reaction)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        reactions = Reaction.objects.all()  
        
        user_id = request.query_params.get('userId', None)
        comment_id = request.query_params.get('commentId', None)
      
        
        if user_id and comment_id is not None:
            for reaction in reactions:
                id = reaction.id
                reaction.clicked = len(CommentReaction.objects.filter(user_id = user_id, comment_id = comment_id, reaction_id = id)) > 0
                reaction.count = len(CommentReaction.objects.filter(reaction_id = id, comment_id = comment_id))
        
        
        serializer = ReactionSerializer(reactions, many = True)
        return Response(serializer.data)
      
      # I dont think the destroy and update is needed 
      # May want to create an add remove 
      # decorator 
      
       
    def create(self, request): 
      '''handels create reaction'''
      reaction = Reaction.objects.create(
        reaction_name = request.data['reaction_name'],
        image_url = request.data['image_url']
      )
      serializer = ReactionSerializer(reaction)
      react_serialized = serializer.data
      react_serialized['image_url'] = react_serialized.pop('image_url')
      
      return Response(react_serialized)
    
    def destroy(self, request, pk):
      '''Handels Delete Request for Reactions'''
      reaction = Reaction.objects.get(pk=pk)
      reaction.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    
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
    
class ReactionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Reaction
        fields = ('id', 'reaction_name', 'image_url', 'clicked', 'count') 
        depth = 1     
