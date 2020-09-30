from rest_framework import serializers

from .models import Account, Userr


# User = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userr
        fields = ['id', 'email','login_type',]


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'firstname', 'lastname', 'passowrd1', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'firstname', 'lastname', 'Favourite']
