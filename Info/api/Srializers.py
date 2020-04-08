from rest_framework import serializers
from Info.models import Account
from django.db.models import Q




class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'g_id', 'name', 'password']

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            password=self.validated_data['password'],
            g_id=self.validated_data['g_id'],
        )
        account.save()
        return account

    def checkExist(self):
        return Account.objects.filter(email=self.validated_data['email']).first()

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'password']

    def check(self):
        account = Account.objects.filter(email=self.validated_data['email'],password=self.validated_data['password']).order_by('-id')

        print( account.first() != None )
        field_object = Account._meta.get_field('id')
        if account.first()!= None and account.count() > 0:
            return getattr(account.first(), field_object.attname)
        else:
            return -1


