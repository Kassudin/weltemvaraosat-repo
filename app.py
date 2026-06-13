from flask import Flask
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

secret_key = getenv("SECRET_KEY")
if not secret_key:
    raise RuntimeError("SECRET_KEY environment variable is required")

app.secret_key = secret_key

import routes

# inject csrf_token() into templates and enforce auth+CSRF before requests
from flask import redirect, request
import user


@app.context_processor
def inject_csrf():
	return {"csrf_token": user.generate_csrf_token}


@app.before_request
def require_login_and_check_csrf():
	# allow login page and static files without auth
	if request.endpoint in (None, 'static'):
		return
	if request.path.startswith('/login'):
		# allow login page
		return

	# require authentication for all other routes
	if not user.is_authenticated():
		return redirect('/login')

	# For POST requests, validate CSRF token
	if request.method == 'POST':
		token = request.form.get('csrf_token') or request.headers.get('X-CSRF-Token')
		if not user.validate_csrf(token):
			return ('CSRF validation failed', 400)