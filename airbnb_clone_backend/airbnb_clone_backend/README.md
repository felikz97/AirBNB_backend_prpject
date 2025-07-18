# 🏡 AirBnB Clone Backend

This is the backend of a full-stack AirBnB clone built with **Django** and **Django REST Framework**. It provides RESTful and GraphQL APIs for managing users, properties, bookings, payments, reviews, and messaging. It also features caching, JWT authentication, search/filtering, and PostgreSQL integration.

---

## 📦 Tech Stack

| Layer        | Technology                      |
|--------------|----------------------------------|
| Framework    | Django, Django REST Framework    |
| DB           | PostgreSQL                       |
| Auth         | JWT (SimpleJWT)                  |
| Async Tasks  | Celery + Redis                   |
| Caching      | Redis                            |
| Deployment   | Railway / Docker (optional)      |
| Docs         | DRF + Swagger/OpenAPI            |

---

## ⚙️ Features

- User authentication (JWT)
- Property management with images
- Booking and availability logic
- Payment flow (mock or Stripe-ready)
- Reviews system
- Secure APIs with throttling and logging
- Search, filtering, and pagination
- Admin panel for all models
- Environment-based configuration via `.env`

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/airbnb-clone-backend.git
cd airbnb-clone-backend
