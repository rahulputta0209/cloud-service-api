import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# ===========================
# Load environment variables
# ===========================
load_dotenv()

# ===========================
# MongoDB Configuration
# ===========================
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URI or not DB_NAME:
    raise EnvironmentError("Missing MONGODB_URI or DB_NAME in environment variables.")

# ===========================
# Database Client
# ===========================
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
