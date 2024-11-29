# GuestBook App

- Run Migrations
```shell
python manage.py migrate
``` 

- Start server

```shell
 python manage.py runserver
``` 

- Generate Random 500 Entries
```shell
  chmod +x generate.sh
  ./generate.sh
```


- 1- Create Entry Request Example
```shell
    curl -X POST http://127.0.0.1:8000/api/entries \
  -H "Content-Type: application/json" \
  -d '{
        "user_name": "Ali Veli",
        "subject": "Yeni Giriş",
        "message": "Bu bir test mesajıdır.",
        "created_date": "2024-11-29"
      }'
``` 

- 2- Get Entries
```shell
curl -X GET http://127.0.0.1:8000/api/entries \
  -H "Content-Type: application/json"
 ```

- 3- Get Users
```shell
curl -X GET http://127.0.0.1:8000/api/users \
  -H "Content-Type: application/json"
```