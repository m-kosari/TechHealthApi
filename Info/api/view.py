from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Info.api.Srializers import RegistrationSerializer , LoginSerializer

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid() and not serializer.checkExist():
            account = serializer.save()
            data['status'] = True
            data['id'] = account.id
        else:
            data['status'] = False
            data['id'] = -1
        return Response(data)


@api_view(['POST',])
def Login_view(request):

    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        data = {}

        serializer.is_valid()
        account = serializer.check()
        if serializer.is_valid() and account != -1:
            data['status'] = True
            data['id'] = account
        else:
            data['status'] = False
            data['id'] = -1
        return Response(data)