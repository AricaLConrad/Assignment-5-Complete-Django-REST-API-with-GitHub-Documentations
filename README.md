# Assignment 5: Complete Django REST API with GitHub Documentations - Instructions

Arica Conrad

BIT 465 - REST API Development

March 5, 2022

Assignment 5: Complete Django REST API with GitHub Documentations

## Introduction

This assignment is to help you build upon the skills you have acquired from Assignment 4 and the first 4 chapters of Building RESTful Python Web Services. See the submission section for more information about what you should submit for this assignment.

## Specification

You should build a new API endpoint that allows an end user to create a new Dog model by making a POST to `/api/dogs,` view current dogs that have been saved to the server before by making a GET to `/api/dogs,` and get, modify, or delete an existing Dog record by making a GET, PUT, or DELETE request (respectively) to `/api/dogs/<id>` where `<id>` is the id of the Dog record to be retrieved, modified, or deleted. Since a Dog includes a foreign key to the breed, you also need to make the same type of endpoints for dog breed at `/api/breeds/` and `/api/breeds/<id>.`
  
## Dog Model
  
A dog should contain the following fields:

- Name (a character string).
- Age (an integer).
- Breed (a foreign key to the Breed Model).
- Gender (a character string).
- Color (a character string).
- Favoritefood (a character string).
- Favoritetoy (a character string).

## Breed Model

A breed should contain the following fields:

- Name (a character string).
- Size (a character string -> should accept Tiny, Small, Medium, or Large).
- Friendliness (an integer field -> should accept values from 1-5).
- Trainability (an integer field -> should accept values from 1-5).
- Sheddingamount (an integer field -> should accept values from 1-5).
- Exerciseneeds (an integer field -> should accept values from 1-5).

## To-Do List

To do this, do the following:

- Track all your changes using GitHub. 
- Add a Dog and Breed models to `models.py`.
- Migrate your database to include tables for Dog and Breed.
- Add two class-based API view controllers for handling Dog REST endpoints to `controllers.py`.
  - All one DogDetail and one DogList to conform to best practice nomenclature.
  - The DogDetail class should have three methods named get, put, delete.
  - The DogList class should have two methods named get and post.
  - Refer to Chapter 2 of the recommended text or [here](https://www.django-rest-framework.org/tutorial/3-class-based-views/) for examples.
- Add two class-based API view controllers for handling Breed REST endpoints to `controllers.py`.
  - Call one BreedDetail and one BreedList to conform to best practice nomenclature.
  - The BreedDetail class should have three methods named get, put, delete.
  - The BreedList class should have two methods named get and post.
  - Refer to Chapter 2 of the recommended text or [here](https://www.django-rest-framework.org/tutorial/3-class-based-views/) for examples.
- Add the appropriate url patterns to the `urls.py` file to accept all the patterns and map them to the correct controller.
- Test your endpoints with POSTMAN/web browser (browsable APIs), taking screenshots of each type of request. There should be 5 requests total for each type of model, for a total of 10 tests and screenshots.
  - GET (list), POST to `/api/dogs/`.
  - GET, PUT, DELETE to `/api/dogs/<id>`.
  - GET (list), POST to `/api/breeds/`.
  - GET, PUT, DELETE to `/api/breeds/<id>`.

## Submission

Submit a Word document containing a link to your GitHub repository for this assignment along with the requirements in the grading rubric.

## Completing This Assignment

There were times when completing this assignment that I had to research solutions to errors I was encountering. I also researched some Django concepts to better understand the function behind each line of code I wrote. You can view some of these sources below.

- <https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl>
- <https://www.django-rest-framework.org/api-guide/fields/>
- <https://www.django-rest-framework.org/api-guide/serializers/>
- <https://www.django-rest-framework.org/tutorial/3-class-based-views/>
- <https://docs.djangoproject.com/en/4.0/topics/db/models/>
- <https://docs.djangoproject.com/en/4.0/topics/http/urls/>
- <https://stackoverflow.com/questions/2642613/what-is-related-name-used-for#:~:text=The%20related_name%20attribute%20specifies%20the%20name%20of%20the,with%20the%20suffix%20_set%2C%20for%20instance%20User.map_set.all%20%28%29>
- <https://stackoverflow.com/questions/27484344/assertion-error-at-django-rest-framework>
- <https://stackoverflow.com/questions/3691101/what-is-the-purpose-of-str-and-repr>
- <https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django>
- <https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model>
- <https://wsvincent.com/django-rest-framework-react-tutorial/>

## Reflection

I gained more knowledge of the Django framework and creating a REST API from scratch on my own. In particular, I learned how to specify and limit specific values for fields, connect the models, views, and urls together, and how to keep a secret key private.  
