# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
	now = datetime.datetime.now()
	return render_to_response('home.html',{'time':now})