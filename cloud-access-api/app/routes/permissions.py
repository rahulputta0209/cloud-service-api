from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from typing import List

from app.db import db
from app.models.permission import PermissionCreate
from app.routes.auth import get_current_user

router = APIRouter()

# ===========================
# Utilities
# ===========================

def serialize_permission(permission: dict) -> dict:
    """Convert MongoDB document to serializable format."""
    permission["id"] = str(permission["_id"])
    permission.pop("_id", None)
    return permission

def admin_only(user: dict = Depends(get_current_user)):
    """Ensure only admins can access certain routes."""
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")

# ===========================
# Routes
# ===========================

@router.post("/", status_code=201, dependencies=[Depends(admin_only)])
async def create_permissions(permissions: List[PermissionCreate]):
    """Create one or more permissions (Admin only)."""
    created_ids = []
    for perm in permissions:
        if await db.permissions.find_one({"name": perm.name}):
            continue
        result = await db.permissions.insert_one(perm.dict())
        created_ids.append(str(result.inserted_id))

    if not created_ids:
        raise HTTPException(status_code=400, detail="No new permissions were created. All names already exist.")

    return {
        "message": f"{len(created_ids)} permissions created successfully",
        "ids": created_ids
    }

@router.get("/", status_code=200)
async def get_all_permissions():
    """Retrieve all permissions."""
    cursor = db.permissions.find()
    return [serialize_permission(doc) async for doc in cursor]

@router.get("/{permission_id}", status_code=200)
async def get_permission(permission_id: str):
    """Get a specific permission by ID."""
    try:
        permission = await db.permissions.find_one({"_id": ObjectId(permission_id)})
        if not permission:
            raise HTTPException(status_code=404, detail="Permission not found")
        return serialize_permission(permission)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid permission ID format")

@router.put("/{permission_id}", status_code=200, dependencies=[Depends(admin_only)])
async def update_permission(permission_id: str, updated: PermissionCreate):
    """Update a permission (Admin only)."""
    result = await db.permissions.update_one(
        {"_id": ObjectId(permission_id)},
        {"$set": updated.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Permission not found or no changes made.")
    return {"message": "Permission updated successfully"}

@router.delete("/{permission_id}", status_code=200, dependencies=[Depends(admin_only)])
async def delete_permission(permission_id: str):
    """Delete a permission by ID (Admin only)."""
    result = await db.permissions.delete_one({"_id": ObjectId(permission_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Permission not found")
    return {"message": "Permission deleted successfully"}
