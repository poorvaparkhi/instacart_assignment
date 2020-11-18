from django.test import TestCase
from ..models import TeamMember


class TeamMemberTest(TestCase):
    """ Test module for TeamMember model """

    def setUp(self):
        TeamMember.objects.create(
            first_name='Poorva', last_name='Parkhi', phone_number=9990361047, role='Admin',
            email='poorvaparkhi@gmail.com')
        TeamMember.objects.create(
            first_name='Apoorva', last_name='Nair', phone_number=9938328047, role='Regular',
            email='apoorvan@gmail.com')

    def test_team_member(self):
        team_member_admin = TeamMember.objects.get(first_name='Poorva')
        team_member_regular = TeamMember.objects.get(first_name='Apoorva')
        self.assertEqual(
            team_member_admin.get_team_member_information(), "Poorva Parkhi having phone number 9990361047 and role: Admin.")
        self.assertEqual(
            team_member_regular.get_team_member_information(), "Apoorva Nair having phone number 9938328047 and role: Regular.")

