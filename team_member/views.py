from team_member.models import TeamMember
from team_member.serializers import TeamMemberSerializer
from rest_framework import mixins
from rest_framework import generics


class TeamMemberList(mixins.ListModelMixin,
                     generics.GenericAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TeamMemberDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
