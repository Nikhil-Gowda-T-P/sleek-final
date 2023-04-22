from flask import Flask, render_template, request, redirect, url_for, make_response
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Define a dictionary of users with their credentials
users = {
	'user1': 'password1',
	'user2': 'password2',
	'user3': 'password3'
}

# Define the secret key for JWT encoding and decoding
JWT_SECRET_KEY = 'myjwtsecret'

# Define the token expiration time in seconds
TOKEN_EXPIRATION_TIME = 300

# Define the function to generate a JWT token for a given user
def generate_token(username):
	payload = {
		'username': username,
		'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKEN_EXPIRATION_TIME)
	}
	return jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

# Define the function to decode a JWT token and extract the username
def decode_token(token):
	try:
		payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
		return payload['username']
	except:
		return None

# Define the login route
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username in users and users[username] == password:
			token = generate_token(username)
			response = make_response(redirect(url_for('secret')))
			response.set_cookie('access_token', token)
			return response
		else:
			return render_template('login.html', message='Invalid username or password')
	else:
		token = request.cookies.get('access_token')
		if token:
			username = decode_token(token)
			if username:
				return redirect(url_for('secret'))
		return render_template('login.html')

# Define the secret route
@app.route('/secret')
def secret():
	token = request.cookies.get('access_token')
	if not token:
		return redirect(url_for('login'))
	username = decode_token(token)
	if not username:
		return redirect(url_for('login'))
	return render_template('secret.html')

# Define the logout route
@app.route('/logout', methods=['POST'])
def logout():
	response = make_response(redirect(url_for('login')))
	response.set_cookie('access_token', '', expires=0)
	return response

if __name__ == '__main__':
	app.run('debug'==True)
	
