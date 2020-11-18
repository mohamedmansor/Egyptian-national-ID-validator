# NID Validator

[![codecov](https://codecov.io/gh/mohamedmansor/Egyptian-national-ID-validator/branch/main/graph/badge.svg?token=FB8DUJS8L6)](https://codecov.io/gh/mohamedmansor/Egyptian-national-ID-validator)

NID validator is a  Django project based API that will validate the National ID number.

# Features!
- It will validate Egyption National ID Number.
    > - Check length
    > - Check NID number combonents is valid.
- Extract User data from the number
    > - Birthdate
    > - Gender
    > - Governorate

### Installation

NID Validator requires [Python v3+](https://www.python.org/download/releases/3.0/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) to be installed.

After creating a virtual

```sh
$ git clone https://github.com/mohamedmansor/plat-course.git
$ cd Egyptian-national-ID-validator
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```
### Development
Run the project:
```sh
$ cd nid_validator
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```
### Test the API

Open postman or any other API testing software.
create a `POST` request to `127.0.0.1:8000/api/v1/nid/validate`
with request body
```json
{
    "national_id_number": "<National-id-number>"
}
```

License
----

MIT

# contributions
To contribute user Django command to create another app then add the validation. create another Django app with added logic of other countries National IDs
