
#  [Oqtepa Lavash Clone](https://oqtepalavash.uz/)

### Oqtepa Lavash saytining Backend qismi API
<img src="https://telegra.ph/file/6d45f443910e44cd0396e.png">
<img src="https://telegra.ph/file/89086569cff3b08c9d345.png">
<img src="https://telegra.ph/file/1ec2dcaa18a0e839ae6e0.png">

## Documentation

### Env o'zgaruvchilari
```python
SECRET_KEY=DJANGO_PROJECT_SECRET_KEY
DB_NAME=your_database_name
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=your_database_host
DB_PORT=5432
REDIS_URL=redis_url
REDIS_TIMEOUT=300 # in second
```
## Bazi o'zgarishlar *
Auth qismi parol va username emas balki telefon raqam va unga keluvchi kod orqali tasdiqlashda userga acess token va refresh token beriladi va boshqa API lar odatdagidek.

# Foydalanilgan Texnologiyalar


<p>
  <a>
    <img src="https://skillicons.dev/icons?i=python,django,sqlite,redis, Postman" />
  </a>
</p>

* Django
* DjangoRestFramework
* Redis
* SQLite
## Some API Docs 

### Telefon raqamga sms (code) yuborish 

```http
  POST /api/user/send_code/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `phone` | `string` | `Required` * |

*__example__*
      
    "phone": "901001010"


*__return__*

    "message": "Sms yuborildi!"

### Login qilish

```http
  POST /api/user/login/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `phone`      | `string` | `Required` * |
| `code`      | `integer` | `Required` * |

*__example__*


    "phone": "901001010",  
    "code": 2010


*__return__*

    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjEyNjkxOCwiaWF0IjoxNjk1ODY3NzE4LCJqdGkiOiJmODBiMzNmM2E3NjA0YWQ4OWNlY2U5ZTAzNDZhNTU1ZCIsInVzZXJfaWQiOjF9.-hRCxoMr0W0Li_K-TMMXTv8jEYUFmTIYiKSGv9ibNRI",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1OTEwOTE4LCJpYXQiOjE2OTU4Njc3MTgsImp0aSI6ImQwM2Y2MmVmODgxNjRlNGU4NTgwMDU4ODUxZmJlZWY3IiwidXNlcl9pZCI6MX0.Uy_WninfaNhKyBjWyUnSigfCiJF3cxdkL6o5_UAGExg"
## Support

For support, email khasanjon.dev@gmail.com or telegram user [@khasanjon_dev](https://t.me/khasanjon_dev) .

