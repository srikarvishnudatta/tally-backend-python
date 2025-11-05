from fastapi import Request
def validate_cookie(request: Request):
    request.cookies.get("access_token")