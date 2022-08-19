# Movie rentals test

Test using django, drf and openapi

## Settings

In order to execute the project you need to complete the following steps:

* Create a **.env** file with the envs: **SECRET_KEY** and **DEBUG**
* Run and apply migrations:
  ```bash
  python manage.py makemigrations & python manage.py migrate
  ```

## Execution

```bash
python manage.py runserver
```

## Additional info

* Home path: `<HOST>:/movies`
* Api prefix: `<HOST>/api/v1`
* Openapi path: `<HOST>:/swagger`
