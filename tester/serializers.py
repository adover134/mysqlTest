from rest_framework import serializers
from tester.models import User


class UserSerializer(serializers.ModelSerializer):
    childrenNames = serializers.ListField(
        child=serializers.CharField()
    )
    pointNumbers = serializers.ListField(
        child=serializers.IntegerField()
    )
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["name", "childrenNames", "pointNumbers"]