# 4x4 Mechanics Garage 🔧

A full-stack **Python Flask** web application for **4x4 Mechanics Garage**, Nashik.

**Owner:** Shantanu Pawar  
**Location:** Amrutdham, Nashik, Maharashtra  
**Contact:** 9403666931

---

## Features

- Public website with all garage services
- Online booking form (saves to JSON)
- Admin panel to manage bookings, services, reviews, and settings
- Mobile responsive design
- WhatsApp booking integration

## Tech Stack

| Layer    | Technology        |
|----------|-------------------|
| Backend  | Python 3 + Flask  |
| Frontend | HTML, CSS, JS     |
| Database | JSON files        |
| Styling  | Custom CSS        |

## Project Structure

```
4x4mechanics/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   ├── index.html      # Public website
│   ├── admin.html      # Admin dashboard
│   └── login.html      # Admin login page
├── static/
│   ├── style.css       # Stylesheet
│   └── script.js       # JavaScript
└── data/
    ├── bookings.json   # Customer bookings
    ├── services.json   # Service list
    ├── reviews.json    # Customer reviews
    └── settings.json   # Business settings
```

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/4x4mechanics.git
cd 4x4mechanics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open in browser
# Public site:  http://localhost:5000
# Admin panel:  http://localhost:5000/admin
```

## Admin Login

- **Username:** `admin`
- **Password:** `4x4admin@2026`

## API Endpoints

| Method | Endpoint                    | Description          |
|--------|-----------------------------|----------------------|
| GET    | `/`                         | Public website       |
| POST   | `/api/book`                 | Submit booking       |
| GET    | `/api/services`             | Get all services     |
| GET    | `/api/reviews`              | Get all reviews      |
| GET    | `/admin`                    | Admin dashboard      |
| POST   | `/admin/bookings/update`    | Update booking status|
| POST   | `/admin/services/add`       | Add new service      |
| POST   | `/admin/reviews/add`        | Add new review       |
| POST   | `/admin/settings/save`      | Save settings        |

---

Made with Python + Flask for **4x4 Mechanics Garage**, Nashik 🚗
