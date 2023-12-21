from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    msg = """<title>TEST</title>
             <h1><b>TEST</b><h1>"""
    return HttpResponseNotFound(msg)
