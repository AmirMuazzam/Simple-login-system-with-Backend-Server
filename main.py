from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel

# Create an instance of the FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the User model
class User(BaseModel):
    username: str
    password: str

# Define the login endpoint
@app.post("/login")
def login(user: User):
    # Connect to the database
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Execute the query to check if the user exists and the password matches
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (user.username, user.password))
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    conn.close()

    # Check the query result
    if result:
        # Return a success response
        return {"success": True, "message": "Login successful!"}
    else:
        # Return an error response
        raise HTTPException(status_code=401, detail="Invalid username or password")





#[3]
# app = FastAPI()

# # Enable CORS
# origins = [
#     "http://localhost",
#     "http://localhost:8000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Connect to the SQLite database
# conn = sqlite3.connect("users.db")
# cursor = conn.cursor()

# @app.post("/login")
# def login(username: str, password: str):
#     # Query the database for the user
#     cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
#     user = cursor.fetchone()

#     # Check if the user exists and the password matches
#     if user and user[1] == password:
#         # Return a success response
#         return {"success": True, "message": "Login successful!"}
#     else:
#         # Return an error response
#         raise HTTPException(status_code=401, detail="Invalid username or password")

# # Close the database connection after the application stops
# @app.on_event("shutdown")
# def shutdown():
#     cursor.close()
#     conn.close()


#[2]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Dummy user for testing
# dummy_user = {
#     "username": "dummyuser",
#     "password": "dummypassword"
# }

# # API endpoint for login
# @app.post("/login")
# def login(credentials: dict):
#     username = credentials.get("username")
#     password = credentials.get("password")

#     # Check if the user exists and the password matches
#     if username == dummy_user["username"] and password == dummy_user["password"]:
#         # Return a success response
#         return {"success": True, "message": "Login successful!"}
#     else:
#         # Return an error response
#         raise HTTPException(status_code=401, detail="Invalid username or password")




#[1]
# @app.get("/")
# def root():
#     return {"message": "Hello, World!"}

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/login")
# async def login(username: str, password: str):
#     # Implement your login logic here
#     # Validate the username and password against the stored credentials
#     # Return a response indicating success or failure

#     # Connect to the SQLite database
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()

#     # Retrieve the user from the database based on the username
#     query = "SELECT * FROM users WHERE username = ?"
#     cursor.execute(query, (username,))
#     user = cursor.fetchone()

#     # Check if the user exists and the password matches
#     if user and user[1] == password:
#         # Return a success response
#         return {"success": True, "message": "Login successful!"}
#     else:
#         #Return an error response
#         raise HTTPException(status_code=401, detail="Invalid username or password")

#     # Close the database connection
    
#     conn.close()
#     cursor.close()