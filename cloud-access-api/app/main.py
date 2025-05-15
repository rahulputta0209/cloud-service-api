from fastapi import FastAPI
from app.routes import (
    plans,
    permissions,
    subscriptions,
    access_control,
    usage,
    auth,
    cloud_apis,
    users
)

# Create FastAPI instance
app = FastAPI(
    title="Rahul-Ibad-Sasidhar's Cloud Service Access Management System"
)

# Register all routers with appropriate prefixes and tags
routes_config = [
    (plans.router, "/plans", ["Plans"]),
    (permissions.router, "/permissions", ["Permissions"]),
    (subscriptions.router, "/subscriptions", ["Subscriptions"]),
    (access_control.router, "/access", ["Access Control"]),
    (usage.router, "/usage", ["Usage Tracking"]),
    (auth.router, "", ["Authentication"]),
    (cloud_apis.router, "", ["Cloud Services"]),
    (users.router, "/users", ["Users"])
]

for router, prefix, tags in routes_config:
    app.include_router(router, prefix=prefix, tags=tags)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Rahul-Ibad-Sasidhar's Cloud Service Access Management System"}
