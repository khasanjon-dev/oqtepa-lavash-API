
#  [Oqtepa Lavash Clone](https://oqtepalavash.uz/)

### Oqtepa Lavash saytining Backend qismi API
## Documentation

### Env o'zgaruvchilari
```python
SECRET_KEY=django-insecure-p-30qi!zhl(nalxwvaaflw!tatf*i2^1y#-71)&y=dasfds=3b
DB_NAME=your_database_name
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://127.0.0.1:6379
REDIS_TIMEOUT=300 # in second
```
## Bazi o'zgarishlar
Auth qismi parol va username emas balki telefon raqam va unga keluvchi kod orqali tasdiqlashda userga acess token va refresh token beriladi va boshqa API lar odatdagidek.

# Foydalanilgan Texnologiyalar

<p>
  <a>
    <img src="https://skillicons.dev/icons?i=python,django,docker,postgres,redis, Postman" />
  </a>
</p>

* Django
* DjangoRestFramework
* Redis
* Postgres
* Docker
## Some API Docs 

### Telefon raqamga sms (code) yuborish 

```http
  POST /api/user/send_code/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `phone` | `string` | `Required` * |

*__example__*

`{"phone": "901001010"}`

### Login qilish

```http
  POST /api/user/login/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `phone`      | `string` | `Required` * |
| `code`      | `integer` | `Required` * |

*__example__*

`{"phone": "901001010", "code": "2010"}`
## Support

For support, email khasanjon.dev@gmail.com or telegram user [@khasanjon_dev](https://t.me/khasanjon_dev) .

