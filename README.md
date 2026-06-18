# URL Shortener

A full-stack URL Shortener application built with **React**, **Flask**, and **SQLite**. Users can shorten long URLs, generate unique short links, redirect using the short URL, and view click analytics for each shortened link.

---

## Features

- Create short URLs from long URLs
- Automatically generate unique short codes
- Redirect users to the original URL
- Track the number of clicks for each shortened URL
- View analytics for every short URL
- RESTful API architecture
- Responsive React frontend
- SQLite database for persistent storage

---

## Tech Stack

### Frontend
- React
- Axios
- CSS

### Backend
- Flask
- Flask SQLAlchemy
- Flask CORS

### Database
- SQLite

---

## Project Structure

```
url-shortener/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
│   ├── database.db
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## API Endpoints

### Create Short URL

**POST**

```
/api/shorten
```

Request

```json
{
  "url": "https://example.com"
}
```

Response

```json
{
  "shortCode": "abc123",
  "shortUrl": "http://localhost:5000/abc123"
}
```

---

### Redirect

**GET**

```
/<shortCode>
```

Redirects the user to the original URL.

---

### Get Analytics

**GET**

```
/api/analytics/<shortCode>
```

Response

```json
{
  "original_url": "https://example.com",
  "short_code": "abc123",
  "clicks": 12,
  "created_at": "2026-06-17"
}
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd url-shortener
```

---

### Backend Setup

```bash
cd backend

python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the backend

```bash
python app.py
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Database

The application uses **SQLite**.

Tables include:

- URLs
- Analytics (click count)

---

## How It Works

1. User submits a long URL.
2. Flask generates a unique short code.
3. The URL is stored in SQLite.
4. A short URL is returned.
5. Visiting the short URL redirects to the original URL.
6. Every redirect increments the click count.
7. Analytics can be viewed using the analytics endpoint.

---

## Future Improvements

- User authentication
- Custom short aliases
- QR code generation
- URL expiration
- Password-protected links
- Dashboard with charts
- Search and filtering
- Docker support
- Deployment on Render

---

## Screenshots

_Add screenshots of the homepage and analytics page here._

---

## Author

**Drishti Dagar**

GitHub: https://github.com/Dishu3597