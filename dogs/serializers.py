# Sources I Used:
# https://www.django-rest-framework.org/api-guide/fields/
# https://wsvincent.com/django-rest-framework-react-tutorial/

# According to the first link, the serializer translates the data into a 
# JSON format that can be sent over the internet and then used by another 
# entity, like the frontend. It could also allow other developers to access
# it too, depending on the permissions we set.

# We need to access both models (Dog and Breed) from the models.py file.
from rest_framework import serializers
from dogs.models import Breed
from dogs.models import Dog

# This defines the serializer class for the Breed model.
class BreedSerializer(serializers.ModelSerializer):

    # The size of the breed should have four choices to choose from (tiny, small, medium, and large).
    # We want to make sure this field represents those four choices.
    size = serializers.ChoiceField(choices = Breed.SIZE_CHOICES)
    
    class Meta:

        # This class is using the Breed model from the models.py file.
        model = Breed

        # This class is using all the fields from the Breed model in the models.py file.
        # This includes the id field which was created automatically.
        fields = (
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds'
        )

# This defines the serializer class for the Dog model.
class DogSerializer(serializers.ModelSerializer):

    # The breed field is the foreign key to the Breed table.    
    # We want to display the breed's name instead of the breed's id.
    breed = serializers.SlugRelatedField(queryset = Breed.objects.all(), slug_field = 'name')

    # If the gender was a set of specific choices (such as female or male), we would specify the gender field like this:
    # gender = serializers.ChoiceField(choices = Dog.GENDER_CHOICES)

    class Meta:

        # This class is using the Dog model from the models.py file.
        model = Dog

        # This class is using all the fields from the Dog model in the models.py file.
        # This includes the id field which was created automatically.
        fields = (
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favoritefood',
            'favoritetoy'
        )
        