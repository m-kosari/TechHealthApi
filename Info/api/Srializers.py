from rest_framework import serializers
from Info.models import Account, Reports, UserInfo, Package, Statuses, GuestStatuses
from django.db.models import Q


# account section

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
        account = Account.objects.filter(email=self.validated_data['email'],
                                         password=self.validated_data['password']).order_by('-id')

        field_object = Account._meta.get_field('id')
        if account.first() != None and account.count() > 0:
            return getattr(account.first(), field_object.attname)
        else:
            return -1


class DemiseAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'password']

    def delete(self):

        account = Account.objects.filter(email=self.validated_data['email'],
                                         password=self.validated_data['password']).order_by('-id')
        field_object = Account._meta.get_field('id')
        if account.first() is not None and account.count() > 0:
            id = getattr(account.first(), field_object.attname)
            account = Account.objects.get(id=id)
            print(account)
            account.delete()
            return "success"

        else:
            return "failed"


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id_user', 'dev_id', 'dev_name', 'dev_model']

    def save(self):
        userInfo = UserInfo(
            id_user=self.validated_data['id_user'],
            dev_id=self.validated_data['dev_id'],
            dev_name=self.validated_data['dev_name'],
            dev_model=self.validated_data['dev_model'],
        )
        userInfo.save()
        return userInfo

    def check(self):
        account = Account.objects.filter(id=self.validated_data['id_user'])
        if account.first() is not None and account.count() > 0:
            return True
        else:
            return False


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id_user', 'report']

    def save(self):
        report = Reports(
            id_user=self.validated_data['id_user'],
            report=self.validated_data['report'],
        )
        report.save()
        return report

    def check(self):
        account = Account.objects.filter(id=self.validated_data['id_user'])
        if account.first() is not None and account.count() > 0:
            return True
        else:
            return False


class SavePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['pck', 'label', 'sts']

    def save(self):
        package = Package(
            pck=self.validated_data['pck'],
            label=self.validated_data['label'],
            sts=self.validated_data['sts']
        )
        package.save()
        return package

    def checkExist(self):
        return Package.objects.filter(pck=self.validated_data['pck']).first()


class SaveStatusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ['pck', 'id_user', 'date', 'long']

    def save(self):
        status = Statuses(
            pck=self.validated_data['pck'],
            id_user=self.validated_data['id_user'],
            date=self.validated_data['date'],
            long=self.validated_data['long'],
        )
        status.save()
        return status

    def checkExist(self):
        return Account.objects.filter(id=self.validated_data['id_user']).first()


class SaveStatusGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestStatuses
        fields = ['pck', 'dev_id', 'date', 'long']

    def save(self):
        status = GuestStatuses(
            pck=self.validated_data['pck'],
            dev_id=self.validated_data['dev_id'],
            date=self.validated_data['date'],
            long=self.validated_data['long'],
        )
        status.save()
        return status


# view data table serializer
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

    def getAll(self):
        return Package.objects.all()


class StatusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = '__all__'

    def getAll(self):
        return Statuses.objects.all()


class StatusGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestStatuses
        fields = '__all__'

    def getAll(self):
        return GuestStatuses.objects.all()