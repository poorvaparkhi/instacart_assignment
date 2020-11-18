from django.db import models
from django.core.validators import RegexValidator


ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Regular', 'Regular'),
]
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. "
                                     "Up to 15 digits allowed.")


class TeamMember(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(choices=ROLE_CHOICES, default='regular', max_length=100)

    class Meta:
        ordering = ['created_at']

    def get_team_member_information(self):
        return f"{self.first_name} {self.last_name} having phone number {self.phone_number} and role: {self.role}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is added"
