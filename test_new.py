from fastapi import  FastAPI

from typing import List
from pydantic import BaseModel, Field

from Base_data import create_tables, session

with open("password_base.txt", "r") as file_object:
    password = file_object.read().strip()

list_base = password.split(",")

login= list_base[0]
password = list_base[1]
database = list_base[2]

create_tables(login,password,database)
users_base = session(login,password,database)
print(users_base)
app = FastAPI(title = "Test App")

@app.get("/users/{gender}")

def get_users(gender: str,limit:int, offset:int):
    return [user for user in  users_base[offset:][:limit] if user.get('gender') == gender]

@app.get("/users")

def get_users():
    return users_base

class Users(BaseModel):
    id: int
    name: str
    gender: str

@app.post("/users")
def get_users(users: List[Users]):
    users_base.extend(users)
    new_user = users[0]
    print(new_user)
    return {'status': 200, 'data': users_base}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
