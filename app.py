"""
4x4 Mechanics Garage - Flask Web Application
Owner: Shantanu Pawar
Location: Amrutdham, Nashik, Maharashtra
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__, template_folder=".")
app.secret_key = "4x4mechanics_secret_2026"

# ── File paths ──────────────────────────────────────────────
DATA_DIR      = os.path.join(os.path.dirname(__file__), "data")
BOOKINGS_FILE = os.path.join(DATA_DIR, "bookings.json")
SERVICES_FILE = os.path.join(DATA_DIR, "services.json")
REVIEWS_FILE  = os.path.join(DATA_DIR, "reviews.json")
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")

# ── Default data ─────────────────────────────────────────────
DEFAULT_SERVICES = [
    {"id": 1, "icon": "🔧", "name": "General Car Service",     "desc": "Complete inspection and maintenance including filters, fluids, belts and vital components.", "price": "Starting ₹1,499"},
    {"id": 2, "icon": "⚙️", "name": "Engine Diagnostics",      "desc": "Advanced computerized engine scanning using OBD tools to pinpoint any fault quickly.",          "price": "Starting ₹499"},
    {"id": 3, "icon": "🛢️", "name": "Oil Change",              "desc": "Premium engine oil and oil filter replacement recommended for your specific car model.",        "price": "Starting ₹399"},
    {"id": 4, "icon": "🛑", "name": "Brake Repair",            "desc": "Complete brake system service — pads, rotors, fluid flush for safe stopping power.",            "price": "Starting ₹799"},
    {"id": 5, "icon": "🚗", "name": "Suspension Repair",       "desc": "Shock absorbers, struts, springs and alignment correction for a smooth comfortable ride.",      "price": "Starting ₹999"},
    {"id": 6, "icon": "❄️", "name": "AC Service",              "desc": "AC gas refilling, compressor check, condenser cleaning and cooling performance restoration.",   "price": "Starting ₹699"},
    {"id": 7, "icon": "🔋", "name": "Battery Replacement",     "desc": "Battery testing, jump start and replacement with reliable branded batteries with warranty.",    "price": "Starting ₹2,499"},
    {"id": 8, "icon": "⚖️", "name": "Wheel Alignment",        "desc": "Computerized 4-wheel alignment and balancing for even tyre wear and straight driving.",        "price": "Starting ₹599"},
    {"id": 9, "icon": "🚿", "name": "Car Washing",             "desc": "Full exterior wash, interior vacuum, dashboard wipe and tyre shine for showroom look.",        "price": "Starting ₹299"},
    {"id":10, "icon": "🚐", "name": "Pickup & Drop",           "desc": "Too busy? We pick up your car from your location and return it when service is done.",         "price": "Call for rates"},
]

DEFAULT_REVIEWS = [
    {"id": 1, "name": "Amit Deshmukh",  "stars": 5, "text": "Best garage in Nashik! Shantanu bhai fixed my Swift Dzire AC in just 2 hours. Very professional and reasonable price.",         "loc": "Nashik, Swift Dzire owner"},
    {"id": 2, "name": "Priya Kulkarni", "stars": 5, "text": "Engine was making noise for months. 4x4 Mechanics diagnosed and fixed it same day. Highly recommend!",                         "loc": "Nashik, Hyundai i20 owner"},
    {"id": 3, "name": "Ravi Patil",     "stars": 5, "text": "Transparent billing, genuine parts used, quick service. Finally found a garage I can fully trust.",                             "loc": "Nashik, Hyundai Creta owner"},
    {"id": 4, "name": "Snehal Joshi",   "stars": 5, "text": "Got my Honda City full service done here. Very thorough and detailed work. Car drives like new!",                               "loc": "Nashik, Honda City owner"},
    {"id": 5, "name": "Mahesh Gaikwad", "stars": 4, "text": "Good service at reasonable rates. Wheel alignment and brake pads done perfectly. Will come back!",                              "loc": "Nashik, Maruti Baleno owner"},
    {"id": 6, "name": "Kavita Sharma",  "stars": 5, "text": "Used pickup and drop service — very prompt and professional. Car returned spotless with all issues fixed!",                     "loc": "Nashik, Hyundai Verna owner"},
]

DEFAULT_SETTINGS = {
    "business_name": "4x4 Mechanics Garage",
    "owner":         "Shantanu Pawar",
    "phone":         "9403666931",
    "address":       "Amrutdham, Nashik, Maharashtra",
    "hours":         "Mon–Sat: 9:00 AM – 7:00 PM, Sunday: 10:00 AM – 4:00 PM",
    "tagline":       "Nashik ka Trusted Garage",
    "admin_password":"4x4admin@2026",
}

# ── Helper functions ──────────────────────────────────────────
def load_json(filepath, default):
    """Load JSON file, return default if not found."""
    try:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError):
        pass
    return default

def save_json(filepath, data):
    """Save data to JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_services(): return load_json(SERVICES_FILE, DEFAULT_SERVICES)
def get_reviews():  return load_json(REVIEWS_FILE,  DEFAULT_REVIEWS)
def get_bookings(): return load_json(BOOKINGS_FILE, [])
def get_settings(): return load_json(SETTINGS_FILE, DEFAULT_SETTINGS)

def is_admin():
    return session.get("admin_logged_in") is True

# ── Public routes ─────────────────────────────────────────────
@app.route("/")
def index():
    """Main public website."""
    return render_template(
        "index.html",
        services=get_services(),
        reviews=get_reviews(),
        settings=get_settings(),
    )

@app.route("/api/book", methods=["POST"])
def book_service():
    """Accept a booking from the public booking form."""
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "No data received"}), 400

    name  = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    if not name or not phone:
        return jsonify({"success": False, "message": "Name and phone are required"}), 400

    bookings = get_bookings()
    booking  = {
        "id":      len(bookings) + 1,
        "name":    name,
        "phone":   phone,
        "car":     data.get("car", "Not specified"),
        "service": data.get("service", "General Service"),
        "issue":   data.get("issue", ""),
        "status":  "pending",
        "date":    datetime.now().strftime("%d %b %Y, %I:%M %p"),
    }
    bookings.insert(0, booking)
    save_json(BOOKINGS_FILE, bookings)

    return jsonify({"success": True, "message": "Booking saved!", "id": booking["id"]})

@app.route("/api/services")
def api_services():
    return jsonify(get_services())

@app.route("/api/reviews")
def api_reviews():
    return jsonify(get_reviews())

# ── Admin routes ──────────────────────────────────────────────
@app.route("/admin")
def admin():
    if not is_admin():
        return redirect(url_for("admin_login"))
    settings = get_settings()
    return render_template(
        "admin.html",
        bookings=get_bookings(),
        services=get_services(),
        reviews=get_reviews(),
        settings=settings,
    )

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        settings = get_settings()
        if username == "admin" and password == settings.get("admin_password", "4x4admin@2026"):
            session["admin_logged_in"] = True
            return redirect(url_for("admin"))
        error = "Wrong username or password"
    return render_template("login.html", error=error)

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("index"))

@app.route("/admin/bookings/update", methods=["POST"])
def update_booking():
    if not is_admin():
        return jsonify({"success": False}), 403
    data       = request.get_json()
    booking_id = int(data.get("id", 0))
    new_status = data.get("status", "pending")
    bookings   = get_bookings()
    for b in bookings:
        if b["id"] == booking_id:
            b["status"] = new_status
            break
    save_json(BOOKINGS_FILE, bookings)
    return jsonify({"success": True})

@app.route("/admin/bookings/delete", methods=["POST"])
def delete_booking():
    if not is_admin():
        return jsonify({"success": False}), 403
    data       = request.get_json()
    booking_id = int(data.get("id", 0))
    bookings   = [b for b in get_bookings() if b["id"] != booking_id]
    save_json(BOOKINGS_FILE, bookings)
    return jsonify({"success": True})

@app.route("/admin/services/add", methods=["POST"])
def add_service():
    if not is_admin():
        return jsonify({"success": False}), 403
    data     = request.get_json()
    services = get_services()
    new_id   = max((s["id"] for s in services), default=0) + 1
    services.append({
        "id":    new_id,
        "icon":  data.get("icon", "🔧"),
        "name":  data.get("name", ""),
        "desc":  data.get("desc", ""),
        "price": data.get("price", "Call for price"),
    })
    save_json(SERVICES_FILE, services)
    return jsonify({"success": True, "id": new_id})

@app.route("/admin/services/delete", methods=["POST"])
def delete_service():
    if not is_admin():
        return jsonify({"success": False}), 403
    service_id = int(request.get_json().get("id", 0))
    services   = [s for s in get_services() if s["id"] != service_id]
    save_json(SERVICES_FILE, services)
    return jsonify({"success": True})

@app.route("/admin/reviews/add", methods=["POST"])
def add_review():
    if not is_admin():
        return jsonify({"success": False}), 403
    data    = request.get_json()
    reviews = get_reviews()
    new_id  = max((r["id"] for r in reviews), default=0) + 1
    reviews.insert(0, {
        "id":    new_id,
        "name":  data.get("name", ""),
        "stars": int(data.get("stars", 5)),
        "text":  data.get("text", ""),
        "loc":   data.get("loc", "Nashik"),
    })
    save_json(REVIEWS_FILE, reviews)
    return jsonify({"success": True})

@app.route("/admin/reviews/delete", methods=["POST"])
def delete_review():
    if not is_admin():
        return jsonify({"success": False}), 403
    review_id = int(request.get_json().get("id", 0))
    reviews   = [r for r in get_reviews() if r["id"] != review_id]
    save_json(REVIEWS_FILE, reviews)
    return jsonify({"success": True})

@app.route("/admin/settings/save", methods=["POST"])
def save_settings():
    if not is_admin():
        return jsonify({"success": False}), 403
    data     = request.get_json()
    settings = get_settings()
    settings.update({
        "business_name": data.get("business_name", settings["business_name"]),
        "owner":         data.get("owner",         settings["owner"]),
        "phone":         data.get("phone",          settings["phone"]),
        "address":       data.get("address",        settings["address"]),
        "hours":         data.get("hours",          settings["hours"]),
        "tagline":       data.get("tagline",        settings["tagline"]),
    })
    if data.get("new_password"):
        settings["admin_password"] = data["new_password"]
    save_json(SETTINGS_FILE, settings)
    return jsonify({"success": True})

# ── Run ────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Create data dir on startup
    os.makedirs(DATA_DIR, exist_ok=True)
    print("=" * 50)
    print("  4x4 Mechanics Garage - Flask Server")
    print("  Owner: Shantanu Pawar, Nashik")
    print("  Visit: http://localhost:5000")
    print("  Admin: http://localhost:5000/admin")
    print("=" * 50)
    app.run(debug=True, port=5000)
