
import sys
try:
    from models import TodoCreate, TodoInDB
    from bson import ObjectId
    print("Import successful")
    
    # Test Pydantic v2 compatibility
    try:
        oid = ObjectId()
        todo = TodoInDB(title="Test", completed=False, _id=oid)
        print(f"Model creation successful: {todo}")
        print(f"JSON schema: {TodoInDB.model_json_schema() if hasattr(TodoInDB, 'model_json_schema') else TodoInDB.schema()}")
    except Exception as e:
        print(f"Model creation failed: {e}")

except Exception as e:
    print(f"Import failed: {e}")
