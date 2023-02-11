from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from playeroneapi.models import CommentReaction, Reaction, Comment, User



class CommentReactionView(ViewSet):
  def list(self, request):
    """GET all comment reactions"""
   
    comment_reactions = CommentReaction.objects.all()
    
    serializer = CommentReactionSerializer(comment_reactions, many=True)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Update a productOrder"""
    comment_reaction = CommentReaction.objects.get(pk=pk)
    comment_reaction.user = User.objects.get(pk=request.data["user"])
    comment_reaction.comment = Comment.objects.get(pk=request.data['comment'])
    comment_reaction.reaction = Reaction.objects.get(pk=request.data['reaction'])
    comment_reaction.save()
    return Response({'success': True}, status=status.HTTP_202_ACCEPTED)
  
  def destroy(self, request, pk):
    """Delete a productOrder"""
    comment_reaction = CommentReaction.objects.get(pk=pk)
    comment_reaction.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)


class CommentReactionSerializer(serializers.ModelSerializer):
  # product = ProductSerializer()
  # order = OrderSerializer()

  class Meta:
    model = CommentReaction
    fields = ('id', 'user', 'comment', 'reaction')
