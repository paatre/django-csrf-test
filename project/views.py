from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def csrf_token_view(request):
    token = get_token(request)
    response = HttpResponse(token)
    response["Access-Control-Allow-Origin"] = "http://localhost:8001"
    response["Access-Control-Allow-Credentials"] = "true"
    return response


@require_http_methods(["POST"])
def post_view(request):
    return HttpResponse() 
