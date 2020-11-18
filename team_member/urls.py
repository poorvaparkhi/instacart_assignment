from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from team_member import views

app_name = 'team-member'
urlpatterns = [
    url(r'^teammembers/$', views.TeamMemberList.as_view(), name='list-all-team-members'),
    url(r'^teammembers/(?P<pk>[0-9]+)/$', views.TeamMemberDetail.as_view(), name='team-member-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
