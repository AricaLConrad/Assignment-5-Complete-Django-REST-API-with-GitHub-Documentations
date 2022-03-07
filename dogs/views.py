# Sources I Used:
# https://www.django-rest-framework.org/tutorial/3-class-based-views/

# We will need to access the Dog and Breed models as well as their respective serializer classes.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from dogs.models import Breed
from dogs.models import Dog
from dogs.serializers import BreedSerializer
from dogs.serializers import DogSerializer

# The DogList class that accepts GET (all) and POST methods.
class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog-list'

# The DogDetail class that accepts GET (one), PUT, and DELETE methods.
class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog-detail'

# The BreedList class that accepts GET (all) and POST methods.
class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-list'

# The BreedDetail class that accepts GET (one), PUT, and DELETE methods.
class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-detail'

# What everything is displayed on. Makes the API browsable.
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'dogs': reverse(DogList.name, request=request),
            'breeds': reverse(BreedList.name, request=request),
        })
