# Project Description: Simple Login System with Backend Server

## Introduction

The Simple Login System project aims to demonstrate the implementation of a basic login system with a backend server. The project consists of a simple frontend interface where users can enter their credentials, and a backend server that handles the login authentication process.

## Features

- User Registration: Users can create an account by providing a username and password.
- User Login: Registered users can log in using their credentials.
- Authentication: The backend server verifies the user's credentials and allows access if they are valid.
- Frontend Interface: A user-friendly HTML interface for entering login credentials.

## Technologies Used

- Python: Backend server implementation using the FastAPI framework.
- SQLite: Database management system for storing user information.
- HTML: Frontend interface for user interaction.
- JavaScript: Handling user input and making API requests to the backend server.

## Project Structure

The project consists of the following files:

- `main.py`: Contains the backend server implementation using FastAPI.
- `index.html`: Provides the HTML structure for the frontend login interface.
- `script.js`: Includes the JavaScript code for handling user input and making API requests.
- `create_users_table.py`: A script to create the users table in the SQLite database.
- `requirements.txt`: Lists the required dependencies for the project.

## Setup and Usage

1. Clone the project repository to your local machine.
2. Create a Virtual Environment (Optional)
   It is recommended to create a virtual environment to keep the project dependencies isolated. Although it is optional, it's considered a best practice.

   - Open your terminal or command prompt.
   - Navigate to the project directory.
   '''
   cd 'path'
   '''
   - Create a new virtual environment.
   '''
   python -m venv env
   '''
   - Activate the virtual environment.
   * For Windows:
   '''
   env\Scripts\activate
   '''
   * For macOS/Linux:
   '''
   source env/bin/activate
   '''

3. Install the project dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Run the `create_users_table.py` script to create the users table in the SQLite database.
    The data (login credentials) can be change directly in this .py before execute or on the SQLite browser after has been created
5. Start the FastAPI Server
   Start the backend server by executing the following command:
   ```
   uvicorn main:app --reload
   ```
6. Open the `index.html` file in a web browser to access the frontend login interface.
7. Enter your login credentials and click the "Submit" button to initiate the login process.
8. The frontend will communicate with the backend server to authenticate your credentials.
9. If the credentials are valid, you will receive a success message. Otherwise, an error message will be displayed.
10. 7. Stop the Server
To stop the FastAPI server, press Ctrl + C in the terminal or command prompt where the server is running.
That's it how to run the login system project!

## Notes

- The project uses SQLite as the database management system, which stores user information in a file named `users.db`. 
- Ensure that the backend server is running before trying to log in through the frontend interface.
- Customize the project files (`main.py`, `index.html`, `script.js`) according to your specific requirements and design preferences.
- Feel free to extend the project by adding additional features such as password hashing, user registration validation, or session management.

## Conclusion

The Simple Login System project provides a basic foundation for implementing a login system with a backend server. By following the setup instructions and customizing the project to fit your needs, one can create a functional and secure login system for their applications. The provided code and files serve as a foundation for implementing user authentication and can be further extended and adapted based on specific requirements.

The backend, implemented using FastAPI, handles the logic for user authentication and interacts with the SQLite database to store and retrieve user information. It provides endpoints for user login and includes basic error handling for invalid credentials.

The frontend, implemented using HTML, CSS, and JavaScript, provides a simple user interface where users can enter their login credentials. When the login form is submitted, it sends a request to the backend server for authentication. The server validates the credentials and responds with a success message or an error if the credentials are invalid.

Once the server is running, you can access the login form by opening the index.html file in a web browser. Enter the username and password, and upon submission, the form will send a request to the backend for authentication. The server will respond with a success message or an error, which will be displayed on the webpage.