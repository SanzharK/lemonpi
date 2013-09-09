from rest_framework import serializers
from models import User

# This Serializer class provides a way for us to serialize and deserialize
# instances of our users. Basically turn them into json and from json to objects

class UserSerializer(serializers.Serializer):
    pk = serializers.Field() # Not really sure what this is doing
    name = serializers.CharField(required=True, max_length=100)
    surname = serializers.CharField(required=True, max_length=100)

def restore_object(self, attrs, instance=None):
    """
    Create or update a new User instance
    Note: that if we don't define this method, then deserializing
    data will simply return a dictionary of items
    """
    if instance:
        instance.name = attrs.get('name', instance.name)
        instance.surname = attrs.get('surname', instance.surname)
        return instance
    #Create new instance
    return User(**attrs)

"""
The first part of this class defines fields that can be deserialized/serialized. THe restore object method defines how fully fledged instances get created when deserializing data. Later on will will use the ModelSerializer class
"""
