from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from Info.api.Srializers import RegistrationSerializer, LoginSerializer, DemiseAccountSerializer, ReportSerializer, \
    UserInfoSerializer, SavePackageSerializer, SaveStatusUserSerializer, SaveStatusGuestSerializer, PackageSerializer,\
    StatusUserSerializer, StatusGuestSerializer


@api_view(['POST', ])
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


@api_view(['POST', ])
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


@api_view(['POST', ])
def DeleteAccount_view(request):
    if request.method == 'POST':
        serializer = DemiseAccountSerializer(data=request.data)
        data = {}

        serializer.is_valid()
        if serializer.is_valid():
            data['message'] = serializer.delete()
        else:
            data['message'] = serializer.delete()
        return Response(data)


@api_view(['POST', ])
def Report_view(request):
    if request.method == 'POST':
        serializer = ReportSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            if (serializer.check()):
                report = serializer.save()
                data['message'] = report.report
            else:
                data['message'] = 'user not found'
        else:
            data['message'] = "failed"
        return Response(data)


@api_view(['POST', ])
def userInfo_view(request):
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        data = {}
        if serializer.is_valid() and serializer.check():
            account = serializer.save()
            data['status'] = True
            data['id'] = account.id_user
        else:
            data['status'] = False
            data['id'] = -1
        return Response(data)


@api_view(['POST', ])
def savePck_view(request):
    if request.method == 'POST':
        serializer = SavePackageSerializer(data=request.data)
        data = {}

        if serializer.is_valid() and not serializer.checkExist():
            pack = serializer.save()
            data['status'] = True
            data['id'] = pack.id
        else:
            data['status'] = False
            data['id'] = -1
        return Response(data)


@api_view(['POST', ])
def saveStatusUser_view(request):
    if request.method == 'POST':
        serializer = SaveStatusUserSerializer(data=request.data)
        data = {}

        if serializer.is_valid() and not serializer.checkExist():
            status = serializer.save()
            data['status'] = True
            data['id'] = status.id
        else:
            data['status'] = False
            data['id'] = -1
        return Response(data)


@api_view(['POST', ])
def saveStatusGuest_view(request):
    if request.method == 'POST':
        serializer = SaveStatusGuestSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            pack = serializer.save()
            data['status'] = True
            data['id'] = pack.id
        else:
            data['status'] = False
            data['id'] = -1
        return Response(data)


class showPck_view(ListAPIView):
    queryset = PackageSerializer().getAll()
    serializer_class = PackageSerializer


class showStatusUser_view(ListAPIView):
    queryset = StatusUserSerializer().getAll()
    serializer_class = StatusUserSerializer


class showStatusGuest_view(ListAPIView):
    queryset = StatusGuestSerializer().getAll()
    serializer_class = StatusGuestSerializer