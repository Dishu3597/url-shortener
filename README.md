# URL Shortener

A full-stack URL Shortener application built with **React**, **Flask**, and **SQLite**. The application allows users to shorten long URLs, generate unique short links, redirect to the original URL, and view click analytics for each shortened link through a clean and responsive interface.

---

# Live Demo

* **Frontend:** https://url-shortener-1-f3ke.onrender.com
* **Backend API:** https://url-shortener-c4m9.onrender.com
---

# Features

* Create short URLs from long URLs
* Automatically generate unique short codes
* Redirect users to the original URL
* Track the number of clicks for each shortened URL
* View analytics for every short URL
* RESTful API architecture
* Input validation and error handling
* Responsive React frontend
* SQLite database for persistent storage
* Automated backend tests

---

# Tech Stack

## Frontend

* React
* Axios
* CSS

## Backend

* Flask
* Flask SQLAlchemy
* Flask CORS
* Pytest

## Database

* SQLite

## Deployment

* Render

---

# Project Structure

```text
url-shortener/
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── tests/
│   ├── utils/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
```

---

# API Endpoints

## Create Short URL

**POST**

```
/api/shorten
```

### Request

```json
{
  "url": "https://example.com"
}
```

### Response

```json
{
  "shortCode": "abc123",
  "shortUrl": "https://url-shortener-c4m9.onrender.com/abc123"
}
```

---

## Redirect

**GET**

```
/<shortCode>
```

Redirects the user to the original URL while incrementing the visit count.

---

## Get Analytics

**GET**

```
/api/analytics/<shortCode>
```

### Response

```json
{
  "original_url": "https://example.com",
  "short_code": "abc123",
  "clicks": 12,
  "created_at": "2026-06-17"
}
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Dishu3597/url-shortener.git

cd url-shortener
```

---

## Backend Setup

Navigate to the backend directory.

```bash
cd backend
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
```

**macOS/Linux**

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

**Windows**

```bash
pip install -r requirements.txt
```

**macOS/Linux**

```bash
python3 -m pip install -r requirements.txt
```

### Run the Backend Server

**Windows**

```bash
python app.py
```

**macOS/Linux**

```bash
python3 app.py
```

The backend server will start on:

```
http://localhost:5000
```

---

## Frontend Setup

Open another terminal.

```bash
cd frontend

npm install

npm run dev
```

The frontend will start on:

```
http://localhost:5173
```

---

# Running Tests

Navigate to the backend directory.

```bash
cd backend

pytest
```

---

# Database

The application uses **SQLite** for persistent storage.

The database stores:

* Original URLs
* Generated short codes
* Creation timestamps
* Click counts

---

# How It Works

1. The user submits a long URL.
2. The backend validates the URL.
3. A unique short code is generated.
4. The URL is stored in the SQLite database.
5. A shortened URL is returned.
6. Visiting the shortened URL redirects to the original URL.
7. Every successful redirect increments the click count.
8. Analytics can be retrieved using the analytics endpoint.

---

# Assumptions and Trade-offs

## Assumptions

* Each shortened URL receives a unique randomly generated short code.
* Analytics track only the total number of visits for each shortened URL.
* SQLite is sufficient for local development and assessment purposes.

## Trade-offs

* SQLite was chosen for simplicity and ease of setup instead of a production database such as PostgreSQL.
* User authentication was intentionally omitted to keep the project focused on the assessment requirements.
* Analytics are limited to click count and creation date; advanced metrics such as IP address, browser information, and geolocation are not collected.
* Short URLs use the Render deployment domain, resulting in longer URLs than a custom production domain.

---

# Future Improvements

* User authentication
* Custom short aliases
* URL expiration
* QR code generation
* Password-protected links
* Advanced analytics (browser, IP address, geolocation)
* Search and filtering
* Dashboard with charts
* Docker support
* Custom domain for shorter URLs

---

# Author

**Drishti Dagar**

GitHub: https://github.com/Dishu3597
