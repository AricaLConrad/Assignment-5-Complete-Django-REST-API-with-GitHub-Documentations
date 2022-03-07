# Sources I Used:
# https://docs.djangoproject.com/en/4.0/topics/db/models/
# https://stackoverflow.com/questions/2642613/what-is-related-name-used-for#:~:text=The%20related_name%20attribute%20specifies%20the%20name%20of%20the,with%20the%20suffix%20_set%2C%20for%20instance%20User.map_set.all%20%28%29.
# https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django
# https://stackoverflow.com/questions/3691101/what-is-the-purpose-of-str-and-repr
# Following the third answer for minimum and maximum integer values:
# https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model

# The second import statement is for validating minimum and maximum integer values.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# This class defines the Breed model. 

# The Breed class needs to be listed before the Dog class, because you will get a  
# "NameError: name 'Breed' is not defined" error if it is not listed first. 
# It does not recognize the Dog's foreign key, as it is referencing the Breed model that has 
# not been created yet since it was listed second.

class Breed(models.Model): 

    # The id field is added automatically according to the Django documentation, 
    # so that is why this model does not have a primary key field specified.

    # The name of the breed. Should be a string variable type.
    name = models.CharField(max_length = 200)
    
    # These are the possible size options for the breed.

    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )

    # The size of the breed. Should be a string variable type that only accepts 
    # the sizes tiny, small, medium, and large. The size is defaulted to tiny.
    size = models.CharField(
        max_length = 2,
        choices = SIZE_CHOICES,
        default = TINY
    )

    # The friendliness of the breed. Should be an integer field that only accepts
    # the values from 1 to 5. 
    friendliness = models.IntegerField(
        default = 1,
        validators = [
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    # The trainability of the breed. Should be an integer field that only accepts
    # the values from 1 to 5. 
    trainability = models.IntegerField(
        default = 1,
        validators = [
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    # The shedding amount of the breed. Should be an integer field that only accepts
    # the values from 1 to 5. 
    sheddingamount = models.IntegerField(
        default = 1,
        validators = [
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    # The exercise needs of the breed. Should be an integer field that only accepts
    # the values from 1 to 5. 
    exerciseneeds = models.IntegerField(
        default = 1,
        validators = [
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

# This class defines the Dog model.

class Dog(models.Model):

    # The id field is added automatically according to the Django documentation, 
    # so that is why this model does not have a primary key field specified.

    # The name of the dog. Should be a string variable type.
    name = models.CharField(max_length = 200)

    # The age of the dog. Should be an integer variable type.
    age = models.IntegerField()

    # A foreign key to the Breed table. It represents the breed of the dog.
    breed = models.ForeignKey (
        Breed, 
        related_name = 'dogs', 
        on_delete = models.CASCADE
    )

    # The gender of the dog. Should be a string variable type.
    gender = models.CharField(max_length = 200)

    # Another way of storing the gender is to specify only male or female. I chose to do the way above.

    # FEMALE = 'F'
    # MALE = 'M'

    # GENDER_CHOICES = (
        # (FEMALE, 'Female'),
        # (MALE, 'Male'),
    # )

    # gender = models.CharField(
        # max_length = 2,
        # choices = GENDER_CHOICES,
        # default = FEMALE
    # )

    # The main color of the dog. Should be a string variable type.
    color = models.CharField(max_length = 200)

    # The favorite food of the dog. Should be a string variable type.
    favoritefood = models.CharField(max_length = 200)

    # The favorite toy of the dog. Should be a string variable type.
    favoritetoy = models.CharField(max_length = 200)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
