from pydantic import BaseModel

print("app_exemple_01.py is being imported")

class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True

if __name__ == "__main__":
    print("Running app_exemple_01.py directly")