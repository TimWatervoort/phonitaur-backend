# Phonitaur API

## Endpoints

### /users/
Available routes: __GET__, __POST__

Will return a list of users or your created user if making a post request.

### /users/:id
Available routes: __GET__, __PATCH__, __DELETE__

Returns the requested user with get or patch requests, returns nothing with a delete request.

### /alphabets
Available routes: __GET__

Will return a list of the alphabets.

### /alphabets/:name
Available routes: __GET__

Will return the alphabet with the given name

### /lessons
Available routes: __GET__

Will return all lessons

### /lessons/:language
Available routes: __GET__

Will return all lessons for the given language

### /lesson/:id
Available routes: __GET__

Will return the lesson with the given id

### /questions/
Available routes: __GET__

Will return all questions

### /questions/:id
Available routes: __GET__

Will return the question with the given id

### /api/token/
Available routes: __POST__

Will provide an access token if provided the correct credentials.
