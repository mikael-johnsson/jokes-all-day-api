# Jokes All Day API
This is the Readme for the backend app to the Jokes All Day project.

[Live site](https://jokes-all-day-frontend-26d817bb989c.herokuapp.com)
[API site](https://jokes-all-day-0142d90d5482.herokuapp.com)
[Front end repository](https://github.com/mikael-johnsson/jokes-all-day)


## Database
This project is created with Django React Framework.

![Image of the ERD](assets/documentation/joke_erd.png)
### Profiles
When a user creates an account, a profile is immediately created. It is connected to the Django User model by its Owner field.

### Jokes
Jokes is the most important model of the site. It is connected to Profiles through Author and can also have Ratings and Reports connected to it.

### Ratings
Ratings are created when a user rates another users joke. The rating itself is a FloatField and on the livesite it is given a value by clicking 1-5 stars. It is connected to Profiles by Author and Jokes by Joke.

### Reports
If a user dislikes a joke, they can report it. The report is conncted to Profiles through author and Jokes through Joke.

The Reports serializer has a to_representation function. It transforms the "personal_attack" report reason to "personal attack". As of now, it does not have a to_internal_data function which causes a bit of a problem when on the live site trying to edit a report with the reason "personal_attack". This is to be sorted in a later iteration.

### Followers
A profile can follow another profile, the instance Followers is then created. Followers is connected to Profiles through both Owner and followed.

## Testing
### Code Validation

### Manual testing

## Deployment