from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from playeroneapi.models import User

class UserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        users = User.objects.all()  
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized user instance
        """
        user = User.objects.get(uid=request.data["user_id"])

        user = User.objects.create(
        first_name = request.data["first_name"],
        last_name = request.data["last_name"],
        uid = request.data["uid"],
        about_me= request.data["about_me"],
        user_name = request.data["user_name"],
        tag_line = request.data["tag_line"],
        image_url = request.data["image_url"]
        
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)  

    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.uid = request.data["uid"]
        user.about_me = request.data["about_ne"]
        user.user_name = request.data["user_name"]
        user.tag_line = request.data["tag_line"]
        user.image_url = request.data["image_url"]
        user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'uid', 'about_me', 'user_name', 'tag_line', 'image_url') 
        depth = 1 
