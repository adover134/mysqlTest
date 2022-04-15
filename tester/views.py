from rest_framework.viewsets import ModelViewSet
from tester.serializers import UserSerializer
from tester.models import User


class UserViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(self, request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)