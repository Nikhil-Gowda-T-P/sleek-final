# sleek-final
# Flask Token-Based Login Example

This is a simple Flask application that demonstrates how to implement token-based login using cookies. When a user logs in with a username and password, the server generates a unique token and stores it in a cookie. This token is then used to identify the user on subsequent requests.

## Requirements

To run this application, you'll need the following:

- Python 3.x
- Flask 2.x

## Installation

1. Clone this repository to your local machine using `git clone`.
2. Navigate to the project directory and create a new virtual environment using `python -m venv venv`.
3. Activate the virtual environment using `source venv/bin/activate` on Mac/Linux or `venv\Scripts\activate` on Windows.
4. Install the required packages using `pip install -r requirements.txt`.
5. Run the application using `python app.py`.
6. Open a web browser and navigate to `http://localhost:5000` to view the application.

## Usage

- To log in, enter any username and password in the login form and click the "Log In" button. This will take you to the secret page, where you can see some top secret information.
- If you close the browser and re-open it, you should still be logged in and redirected to the secret page.
- To log out, click the "Logout" button on the secret page. This will remove the token from the cookie and redirect you to the login page.
- If you try to access the secret page without being logged in, you will be redirected to the login page.

## Contributions

This project is open to contributions and pull requests. Please feel free to fork the repository and submit your changes.
