from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

#articles의 메인 페이지, article list를 보여준다.
def index(request):
    #SELECT * FROM articles
    articles =  Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# variable roution 으로 사용자가 보기를 원하는 페이지 pk를 받아서 디페일 페이지에 보여준다.
def detatil(request, article_pk):
    # SELECT * FROM articles WHERE pk=article_pk
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)
# 입력 페이지 제공
def new(request):
    return render(request,'articles/new.html')

#데이터를 전달받아 article 생성
def create(request):

    # articles/new/를 통해 new.html의 form에서 전달받은 데이터 
    title = request.GET.get('title')
    content = request.GET.get('content')

    #우리가 받은 데이터를 DB에 생성하자
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('/articles/%d' %  article.pk )

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')
    

