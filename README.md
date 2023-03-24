VELL MAGAZINE - BACKEND API
==================================

* * *

ABOUT THE API:
------------------

* * * 


[DEPLOYED API HEROKU LINK]()

[DEPLOYED FRONTEND HEROKU LINK - LIVE SITE]()

[DEPLOYED BACKEND GITHUB REPOSITORY]()


This is the Back End API for _Vell Magazine_, created using Django REST Framework. This back end, will return only JSON data.

<img src="src/assets/home.png" width="500px">

So what do we need from our API?

From within the React app, we make HTTP requests to our drf api (which substituted the django context object with JSON responses).
JSON data, which React uses to then render the UI.
CRUD functionality! Create, Retrieve, Update or Delete things like a profile, a class, a booking, etc. This is through the HTTP requests.
Receive responses such as 2xx OK, 4xx ERROR, 5xx SERVER ERROR.

<img src="assets/crudtable.png" width="500px">


* * *

## DJANGO REST FRAMEWORK

* * *

I decided to use Django REST Framework as I can easily make use of its serializers, APIVIew & generics, permissions and authentications. It can serve both mobile and web apps.


Login and Log out views of our API in-browser interface. These come with our REST Framework.


* * * 

# PROFILE APP:

* * *

What functionality to we want?
* Authors have their own profile
* Authors can publish their own articles.
* List all articles for all users to view.
* List all authors for every user to view?



* * *


