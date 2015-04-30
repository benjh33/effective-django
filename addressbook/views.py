from .models import Contact
from django.shortcuts import render, redirect
from django.views.generic import View


class HomeView(View):
    template = 'base.html'
