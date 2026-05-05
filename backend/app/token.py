from rest_framework import authentication


class Token(authentication.TokenAuthentication):
    keyword='Bearer'