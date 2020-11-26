from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import TeamMember
from ..serializers import TeamMemberSerializer
import json


# initialize the APIClient app
client = Client()
TEAM_MEMBERS_URL = reverse('team-member:team-members')


class GetAllTeamMembersTest(TestCase):
    """ Test module for all team members API """

    def setUp(self):
        TeamMember.objects.create(
            first_name='Poorva', last_name='Parkhi', phone_number=9990361047, role='Admin',
            email='poorvaparkhi@gmail.com')
        TeamMember.objects.create(
            first_name='John', last_name='Oliver', phone_number=9938328047, role='Regular',
            email='johnoli@gmail.com')
        TeamMember.objects.create(
            first_name='Adam', last_name='Driver', phone_number=9938328047, role='Regular',
            email='adamdriver@gmail.com')
        TeamMember.objects.create(
            first_name='Christian', last_name='Bale', phone_number=9938328047, role='Regular',
            email='christian_bale@gmail.com')

    def test_get_all_team_members(self):
        # get API response
        response = self.client.get(TEAM_MEMBERS_URL, format='json')
        # get data from db
        team_members = TeamMember.objects.all()
        serializer = TeamMemberSerializer(team_members, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewTeamMemberTest(TestCase):
    """ Test module for inserting a new team member """

    def setUp(self):
        self.valid_payload = {'first_name': 'John', 'last_name': 'Oliver', 'phone_number': 9938328047,
                              'role': 'Regular', 'email': 'johnoli@gmail.com'}

        self.invalid_payload = {'first_name': 'John', 'last_name': 'Oliver', 'phone_number': 'wrong_phone_number',
                                'role': 'Regular', 'email': 'johnoli@gmail.com'}

    def test_create_valid_team_member(self):
        response = self.client.post(
            reverse(TEAM_MEMBERS_URL),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_team_member(self):
        response = self.client.post(
            reverse(TEAM_MEMBERS_URL),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleTeamMemberTest(TestCase):
    """ Test module for getting a single team member API """

    def setUp(self):
        self.admin = TeamMember.objects.create(
            first_name='Poorva', last_name='Parkhi', phone_number=9990361047, role='Admin',
            email='poorvaparkhi@gmail.com')

    def test_get_valid_single_team_member(self):
        response = self.client.get(reverse('team-member:team-member-detail', args=[self.admin.id]), format='json')
        team_member = TeamMember.objects.get(id=self.admin.id)
        serializer = TeamMemberSerializer(team_member)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_team_member(self):
        response = self.client.get(reverse('team-member:team-member-detail', args=[999]), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PutUpdateSingleTeamMemberTest(TestCase):
    """ Test module for put updating an existing team member record """

    def setUp(self):
        self.team_member_three = TeamMember.objects.create(first_name='Christian', last_name='Bale',
                                                           phone_number=9938328047, role='Regular',
                                                           email='christian_bale@gmail.com')
        self.team_member_two = TeamMember.objects.create(
                first_name='Adam', last_name='Driver', phone_number=9938328047, role='Regular',
                email='adamdriver@gmail.com')
        self.valid_payload = {'first_name': 'Christian', 'last_name': 'Bale', 'phone_number': 9938328047,
                              'role': 'Admin', 'email': 'christian_bale@yahoo.com'}
        self.invalid_payload = {'first_name': '', 'last_name': 'Driver', 'phone_number': 9938328047,
                              'role': 'Regular', 'email': 'adamdriver@gmail.com'}

    def test_valid_update_team_member(self):
        response = client.put(
            reverse('team-member:team-member-detail', args=[self.team_member_three.id]),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_team_member(self):
        response = client.put(
            reverse('team-member:team-member-detail', args=[self.team_member_two.id]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PatchUpdateSingleTeamMemberTest(TestCase):
    """ Test module for patch updating an existing team member record """

    def setUp(self):
        self.team_member_three = TeamMember.objects.create(first_name='Christian', last_name='Bale',
                                                           phone_number=8083334443, role='Regular',
                                                           email='christian_bale@gmail.com')
        self.team_member_two = TeamMember.objects.create(
            first_name='Adam', last_name='Driver', phone_number=9938328047, role='Regular',
            email='adamdriver@gmail.com')
        self.valid_payload = {'first_name': 'Christian', 'last_name': 'Bale', 'phone_number': 9938328047,
                              'role': 'Admin', 'email': 'christian_bale@yahoo.com'}
        self.invalid_payload = {'first_name': '', 'last_name': 'Driver', 'phone_number': 9938328047,
                                'role': 'Regular', 'email': 'adamdriver@gmail.com'}

    def test_valid_update_team_member(self):
        response = client.patch(
            reverse('team-member:team-member-detail', args=[self.team_member_three.id]),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_team_member(self):
        response = client.patch(
            reverse('team-member:team-member-detail', args=[self.team_member_two.id]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleTeamMemberTest(TestCase):
    """ Test module for deleting an existing team member record """

    def setUp(self):
        self.team_member_three = TeamMember.objects.create(first_name='Christian', last_name='Bale',
                                                           phone_number=9938328047, role='Regular',
                                                           email='christian_bale@gmail.com')
        self.team_member_two = TeamMember.objects.create(
            first_name='Adam', last_name='Driver', phone_number=9938328047, role='Regular',
            email='adamdriver@gmail.com')
        self.valid_payload = {'first_name': 'Christian', 'last_name': 'Bale', 'phone_number': 9938328047,
                              'role': 'Admin', 'email': 'christian_bale@yahoo.com'}
        self.invalid_payload = {'first_name': '', 'last_name': 'Driver', 'phone_number': 9938328047,
                                'role': 'Regular', 'email': 'adamdriver@gmail.com'}

    def test_valid_delete_team_member(self):
        response = client.delete(
            reverse('team-member:team-member-detail', args=[self.team_member_three.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_team_member(self):
        response = client.delete(
            reverse('team-member:team-member-detail', args=[99]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
