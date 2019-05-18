from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model as User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User().objects.all())])
    username = serializers.CharField(
        max_length=20,
        required=True,
        validators=[UniqueValidator(queryset=User().objects.all())])
    password = serializers.CharField(min_length=8, write_only=True, style={
                                     'input_type': 'password'})
    first_name = serializers.CharField(max_length=60, required=True)
    last_name = serializers.CharField(max_length=60, required=True)

    def create(self, validated_data):
        user = User().objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user

    class Meta:
        model = User()
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'password')
