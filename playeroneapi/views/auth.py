from playeroneapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has associated Profile
    First function that checks inside of the database to see if the user in the dB
    if it is not finding the uid, you get redirectred to the reg user function 
 
    Method arguments:
    request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    playerone_user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token

    if playerone_user is not None:
        data = {
            'id': playerone_user.id,
            'first_name': playerone_user.first_name,
            'last_name': playerone_user.last_name,
            'about_me': playerone_user.about_me,
            'user_name': playerone_user.user_name,
            'tag_line': playerone_user.tag_line,
            'image_url': playerone_user.image_url,
            'uid': playerone_user.uid,
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the bangazonapi_user table
    playerone_user = User.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        user_name=request.data['user_name'],
        tag_line=request.data['tag_line'],
        about_me=request.data['about_me'],
        image_url=request.data['image_url'],
        uid=request.data['uid']
    )

    # Return the user info to the client
    data = {
        'id': playerone_user.id,
        'first_name': playerone_user.first_name,
        'last_name': playerone_user.last_name,
        'user_name': playerone_user.user_name,
        'tag_line': playerone_user.tag_line,
        'about_me': playerone_user.about_me,
        'image_url': playerone_user.image_url,
        'uid': playerone_user.uid,
    }
    return Response(data)
