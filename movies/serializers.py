from rest_framework import serializers
from .models import Movie, RatingChoice, MovieOrder
from users.models import User
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default="null")
    rating = serializers.ChoiceField(
        RatingChoice, default=RatingChoice.G, allow_null=True
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: User) -> str:
        user = UserSerializer(obj.user)
        return user["email"].value

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_buyed_by(self, obj):
        return obj.user.email

    def get_title(self, obj):
        return obj.movie.title

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
