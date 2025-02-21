from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Account,Book,Author

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["first_name"] = user.first_name
        token["isAdmin"] = user.is_superuser

        # ...

        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password",
            "profile_pic",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError({"password": "password is not valid"})


class UserDetailsUpdateSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ["id", "profile_pic", "first_name", "last_name", "email","phone_number"]


class UpdateUserDetial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def update(self,instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
    

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"  # Includes all fields

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), many=True
    ) # Nested serialization

    class Meta:
        model = Book
        fields = "__all__"

    # def create(self, validated_data):
    #     authors_data = validated_data.pop('authors', [])
    #     book = Book.objects.create(**validated_data)
    #     book.authors.set(authors_data)  # Assign authors
    #     return book

    # def update(self, instance, validated_data):
    #     authors_data = validated_data.pop('authors', None)
    #     if authors_data is not None:
    #         instance.authors.set(authors_data)
    #     return super().update(instance, validated_data)