# Ecommerce REST API

A RESTful API for an online shopping platform, developed with **Django** and **Django REST Framework**.

This project provides core e-commerce functionalities, including user authentication, product and category management, shopping carts, order processing, and asynchronous email notifications.

## Features

- **JWT Authentication:** Secure authentication using JSON Web Tokens.
- **User Management:** User account management and authentication.
- **Product Management:** Create, retrieve, update, and manage products.
- **Category Management:** Organize products into categories and subcategories.
- **Shopping Cart:** Add, update, retrieve, and remove cart items.
- **Order Management:** Create and manage customer orders.
- **Checkout:** Convert shopping cart items into orders.
- **Delivery Cost Management:** Configure and manage delivery costs.
- **Asynchronous Tasks:** Background task processing using Celery.
- **Message Broker:** RabbitMQ integration.
- **Email Notifications:** Asynchronous order confirmation emails.
- **API Documentation:** Interactive API documentation with Swagger and ReDoc.
- **Django Admin:** Manage application data through Django Admin.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django 6.1.2 | Backend framework |
| Django REST Framework | REST API development |
| PostgreSQL | Database |
| psycopg | PostgreSQL adapter |
| Simple JWT | JWT authentication |
| Celery | Asynchronous task processing |
| RabbitMQ | Message broker |
| drf-yasg | Swagger and ReDoc documentation |
| django-filter | API filtering |
| Git | Version control |

## Project Structure

```text
Ecommerce-api/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── ...
│
├── accounts/
│   ├── models.py
│   ├── api/
│   └── ...
│
├── products/
│   ├── models.py
│   ├── api/
│   └── ...
│
├── cart/
│   ├── models.py
│   ├── admin.py
│   └── ...
│
├── orders/
│   ├── models.py
│   ├── tasks.py
│   ├── admin.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Ecommerce-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

This project uses PostgreSQL as its primary database.

Configure your database credentials in `core/settings.py`.

Run database migrations:

```bash
python manage.py migrate

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

## Celery and RabbitMQ Configuration

This project uses RabbitMQ as the message broker and Celery to process background tasks.

Start RabbitMQ:

```bash
sudo systemctl start rabbitmq-server
```

Start the Celery worker:

```bash
celery -A core worker -l info
```

## Email Configuration

The project currently uses Django's console email backend for development.

Order confirmation emails are processed asynchronously by Celery and displayed in the Django terminal instead of being sent to real email addresses.

## API Documentation

API documentation is generated using `drf-yasg`.

Available documentation interfaces:

- **Swagger UI:** Interactive API documentation.
- **ReDoc:** API reference documentation.

Run the development server and open the documentation URLs configured in `core/urls.py`.

## Authentication

The API uses JSON Web Tokens (JWT) for authentication through `djangorestframework-simplejwt`.

Clients can authenticate using access and refresh tokens.

## Current Limitations and Future Improvements

- Automated API testing.
- Product inventory management.
- Online payment gateway integration.
- Production email configuration.
- Production deployment.

## Develop by:

**Aref Afkhami**

Computer Engineering Student | Backend Developer

[GitHub Profile](https://github.com/aref-af20)


