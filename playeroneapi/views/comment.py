"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from playeroneapi.models import VideoGame, User, Reaction, Comment
from rest_framework import generics




class CommentView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        comments = Comment.objects.all()  
        
        game_id = request.query_params.get('game_id', None)
        if game_id is not None:
                comments = comments.filter(game_id = game_id)
        
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = User.objects.get(pk=request.data["user"])
        game = VideoGame.objects.get(pk=request.data["game"])
        # reactions = Reaction.objects.get(pk=request.data["reactions"])

        comment = Comment.objects.create(
        comment_title=request.data["comment_title"],
        comment=request.data["comment"],
        date_created=request.data["date_created"],
  
        user=user,
        game=game,
        # reactions=reactions
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        comment = Comment.objects.get(pk=pk)
        comment.comment_title = request.data["comment_title"]
        comment.comment = request.data["comment"]
        comment.date_created = request.data["date_created"]

        # game = VideoGame.objects.get(pk=request.data["game"])
        # comment.game = game
        # reactions = Reaction.objects.get(pk=request.data["reactions"])
        # comment.reactions = reactions
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT) 
    
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'game', 'reactions', 'comment_title', 'comment', 'date_created') 
        depth = 1 

class VideoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGame
        fields = ('id', 'user', 'game_genre', 'game_title', 'purchase_location', 'game_format', 'description', 'image_url') 
        depth = 1             

class CommentGameView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
      game = self.kwargs['game_id']
      return Comment.objects.filter(game__id=game) 
