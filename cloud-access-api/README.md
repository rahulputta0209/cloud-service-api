Cloud Service Access Management System
A FastAPI + MongoDB backend that controls access to simulated cloud services based on user subscription plans. It features JWT authentication, role-based access control, and usage tracking.

Features:

User Registration (open)

JWT Auth (admin/user roles)

Role-Based Access Control

Subscription Plan & Usage Management

6 Simulated Cloud APIs

Admin control for users, permissions, and plans

Project Structure:
bash
Copy
Edit
app/
├── db.py           # MongoDB connection
├── main.py         # FastAPI app entry
├── models/         # Pydantic schemas
├── routes/         # API route definitions
├── services/       # Auth, utils, etc.
Requirements:
Python 3.10+

MongoDB running locally/remotely

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file:

ini
Copy
Edit
MONGODB_URI=mongodb://localhost:27017
DB_NAME=cloud_access
Run the app:

bash
Copy
Edit
uvicorn app.main:app --reload
Docs: http://127.0.0.1:8000/docs

Authentication:
Log in via /token with:

Username: admin

Password: admin123

Role: admin

Use Bearer <token> in Swagger UI.

Key Endpoints:
Auth
POST /token – Get JWT token

Users
POST /users/ – Register (open)

DELETE /users/{username} – Admin only

GET /users/ – Admin only

Permissions & Plans
POST /permissions/ – Admin only

GET /permissions/ – All roles

POST /plans/ – Admin only

GET /plans/ – All roles

Subscriptions:
POST /subscriptions/ – Users/admin

PUT /subscriptions/{user_id} – Own/admin

GET /subscriptions/{user_id} – Own/admin

DELETE /subscriptions/{user_id} – Admin only

GET /subscriptions/{user_id}/usage – Track usage

Access & Cloud APIs
GET /access/{user_id}/{api_name} – Check access

GET /cloud/api1–6/{user_id} – Simulated cloud services

Notes:
Exceeding limits returns 429

Accessing without permissions returns 403

Authors:
Rahul Putta, CS Grad Student, CSU Fullerton

Ibad Ur Rahman Mohammed, CS Grad Student, CSU Fullerton

Sasidhar Jonnalagadda, CS Grad Student, CSU Fullerton
