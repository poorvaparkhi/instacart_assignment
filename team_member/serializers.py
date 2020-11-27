from rest_framework import serializers
from team_member.models import TeamMember
from team_member.models import phone_regex
from team_member.models import ROLE_CHOICES


class TeamMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True, max_length=100)
    last_name = serializers.CharField(required=True, max_length=100)
    phone_number = serializers.CharField(validators=[phone_regex], max_length=17)
    email = serializers.EmailField(max_length=254)
    role = serializers.ChoiceField(choices=ROLE_CHOICES, default='regular')

    def create(self, validated_data):
        """
        Create and return a new `TeamMember` instance, given the validated data.
        """
        return TeamMember.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TeamMember` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
