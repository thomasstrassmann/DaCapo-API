from rest_framework.response import Response
from rest_framework.decorators import api_view
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    return Response({"introduction":
                     "Hello and welcome to the dacapo-rest-api! You can "
                     "access the following endpoints:",
                     "profiles/": "GET",
                     "profiles/id/": "GET, PUT",
                     "instruments/": "GET, POST",
                     "instruments/id/": "GET, PUT, DELETE",
                     "bookmarks/": "GET, POST",
                     "bookmarks/id/": "GET, DELETE",
                     "followers/": "GET, POST",
                     "followers/id/": "GET, DELETE",
                     "wanted/": "GET, POST",
                     "wanted/id/": "GET, PUT, DELETE",
                     "rating/": "GET, POST",
                     "rating/id/": "GET, PUT, DELETE"
                     })


@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
