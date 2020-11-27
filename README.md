#### Team Member Management #####

This app is built using Django Rest framework (3.12.2).
It consists of 4 APIs :
1. get all team members
2. get a single team member
3. update a single team member
4. delete a single team member

##### Setup and testing
1. Install and configure MySQL on your laptop. Create a database `team_member`. Create a user named `djangouser`
with password `password`. Grant all permissions of `team_member` database to this user.
- Also give permissions to
create all databases to this user *(that is needed as unit tests written in ** tests/ ** package need the privileges to run).*

2. Once user and db has been created, run data migration script (in `team_member/migrations/0002_auto_20201118_1645.py`)
that will insert dummy data for you.

3. you can also install and use httpie to hit API end-points and test them. example-usage :

    - `http http://127.0.0.1:8000/teammembers/`
    - `http http://127.0.0.1:8000/teammembers/2/`






