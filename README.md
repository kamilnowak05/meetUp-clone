# meetUp-clone-rest-api
meetUp-clone app rest api source code

# It's my implementation of the meetUp REST API.

## Pre-commit:
To install pre-commit hook, run:
```
pre-commit install
```

Run:
```
pre-commit run --all-files
```


## Features:

-   management user account (register, login, logout, manage)
-   groups (CRUD, join)
-   events (CRUD, join, reviev)
-   categories

## Technology Stack:

-   Python
-   Django and Django Rest Framework
-   PostgreSQL

## Default urls:
- localhost:8000/api/users/register/
- localhost:8000/api/users/login/
- localhost:8000/api/users/logout/
- localhost:8000/api/users/me/
- localhost:8000/api/users/'<slug:id>'/
- localhost:8000/api/groups/list/
- localhost:8000/api/groups/list/?owner=owner
- localhost:8000/api/groups/list/?id=group_id
- localhost:8000/api/groups/create/
- localhost:8000/api/groups/manage/<int:group_id>/
- localhost:8000/api/groups/members/<int:group_id>/
- localhost:8000/api/events/list/
- localhost:8000/api/events/list/?member=member
- localhost:8000/api/events/list/?title=title_icontains
- localhost:8000/api/events/list/?category=category
- localhost:8000/api/events/list/?id=event_id
- localhost:8000/api/events/create/
- localhost:8000/api/events/manage/<int:event_id>/
- localhost:8000/api/events/category/
- localhost:8000/api/events/members/<int:event_id>/
- localhost:8000/api/events/reviev/
- localhost:8000/api/events/reviev/?q=reviev_icontains
- localhost:8000/api/events/reviev/?user=user
- localhost:8000/api/events/reviev/<int:id>
