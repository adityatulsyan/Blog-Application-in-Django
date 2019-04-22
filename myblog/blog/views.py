# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


"""def index(request):
	return HttpResponse("Hello, world. You're at the blog index.")"""

def index(request):
	return HttpResponse("Hello, world. You're at the blogs index.")

def index2(request):
	all_post = Post.objects.all()
	html = ''
	for post in all_post:
		url = '/blog/blogs/' + str(post.id) + '/'
		html+= '<a href="' + url + '">' + post.title + '</a><br>'
	return HttpResponse(html)

def detail(request, id):
	recent_post = Post.objects.get(pk = id)
	return HttpResponse(recent_post.title + ': ' + recent_post.text)