from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer

# Create your views here.
class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        return UserSerializer