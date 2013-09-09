from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import User
from serializers import UserSerializer

class JSONResponse(HttpResponse):
    # A HttpResponse that renders its content to JSON
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def user_list(request):
    print "In the method : %s "  + request.method;
    # lists all of the users or creates a new one
    if request.method == 'GET':
        print "In the GET of user list"
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return HttpResponse(serializer.data)

    elif request.method == 'POST':
        print "In the POST of user list"
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)
        else:
            return HttpResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    # Retrieve, update or delete a user
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JSONResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
