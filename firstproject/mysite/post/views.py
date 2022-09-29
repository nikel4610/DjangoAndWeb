from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import *
from post.models import post
from flask import redirect

# Create your views here.
def index(request):
    return render(request, 'post/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴 
    return render(request, 'post/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'post/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/post/')
    return render(request, 'post/new_post.html')

def remove_post(request, pk):
    post = post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/post/')
    return render(request, 'post/remove_post.html', {'Post': post})