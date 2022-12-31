from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def root_route(request):
    return Response({"introduction":
                     "Hello and welcome to the dacapo-rest-api! You can "
                     "access the following endpoints:",
                     "profiles/": "GET",
                     "profiles/id": "GET, PUT",
                     "instruments/": "GET, POST",
                     "instruments/id": "GET, PUT, DELETE",
                     "bookmarks/": "GET, POST",
                     "bookmarks/id": "GET, DELETE",
                     "followers/": "GET, POST",
                     "followers/id": "GET, DELETE"
                     })
