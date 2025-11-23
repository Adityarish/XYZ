
import asyncio
import sys
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

async def check_mongo():
    try:
        client = AsyncIOMotorClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
        await client.server_info()
        print("Mongo: OK")
        return True
    except Exception as e:
        print(f"Mongo: FAILED ({e})")
        return False

async def check_api():
    try:
        API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{API_BASE_URL}/health", timeout=2.0)
            if resp.status_code == 200:
                print("API: OK")
                return True
            else:
                print(f"API: FAILED (Status {resp.status_code})")
                return False
    except Exception as e:
        print(f"API: FAILED ({e})")
        return False

async def main():
    mongo_ok = await check_mongo()
    api_ok = await check_api()
    if not mongo_ok or not api_ok:
        sys.exit(1)

if __name__ == "__main__":
    # Install httpx if missing (it's not in requirements.txt but useful for testing)
    # Actually, let's use urllib for API to avoid dependency issues if httpx not installed
    # But wait, I can use the venv python which might not have httpx.
    # I'll use urllib.
    pass

import urllib.request
import urllib.error

def check_api_sync():
    API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")
    try:
        with urllib.request.urlopen(f"{API_BASE_URL}/health", timeout=2) as response:
            if response.getcode() == 200:
                print("API: OK")
                return True
    except Exception as e:
        print(f"API: FAILED ({e})")
        return False

# Redefine main to use sync api check
async def main_mixed():
    mongo_ok = await check_mongo()
    api_ok = check_api_sync()
    if not mongo_ok or not api_ok:
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main_mixed())
