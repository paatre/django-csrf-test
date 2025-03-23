# Django CSRF test

This is a simple Django project to test CSRF protection against a CSRF attack using a simple redirect attack with victim's browser to a vulnerable website.

`attacker.html` is the attacker's website that will try to perform the CSRF attack on the Django server. The attacker HTML file is served by a separate Python server supporting POST requests (the default `http.server` doesn't support POST) configured in `server.py`.

The attack is performed by first stealing a CSRF token from a victim by redirecting the victim's browser to a CSRF token endpoint on the Django server. The attacker then uses the stolen CSRF token to perform a POST request to the Django server to a relevant endpoint.

Note that the endpoints also need to send a vulnerable CORS headers for the attack to be able to happen. That's why the following headers are sent during a response:

```http
Access-Control-Allow-Origin: http://localhost:8001
Access-Control-Allow-Credentials: true
```
