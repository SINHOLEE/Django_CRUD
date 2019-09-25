from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment

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
    article = get_object_or_404(Article,pk=article_pk)

    # article에 대한 모든 댓글을 꺼내겠다.
    # comments = article.comment_set.all()
    comments = article.comments.all()


    context = {
        'article' : article,
        'comments' : comments
    }
    return render(request, 'articles/detail.html', context)
# 입력 페이지 제공
# GET /articles/create/
# def new(request):
    # return render(request,'articles/new.html')

#데이터를 전달받아 article 생성
# POST /articles/create/
def create(request):
    # 만약 POST 요청이라면 사용자 데이터를 받아서 articles 생성
    if request.method == 'POST':

         # articles/new/를 통해 new.html의 form에서 전달받은 데이터 
        title = request.POST.get('title')
        content = request.POST.get('content')    
        image = request.FILES.get('image')
        #우리가 받은 데이터를 DB에 생성하자
        article = Article(title=title, content=content, image=image)
        article.save()

        return redirect('articles:detail', article.pk)
    
    # 아니라면(GET)요청으로 들어오면 html 페이지 rendering
    else:
        return render(request,'articles/create.html')

       

def delete(request, article_pk):
    if request.method == "POST":
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)
    
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)


    # POST로 들어왔을 때에는 실제 update 로직이 수행할 수 있도록하자.
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image') # 만약 아무것도 안넘어 왔다면, 이미지를 수정하지 않겠다.
                                           # 만약 어떤것이 넘어 왔다면, 이미지를 수정하겠다.
        
        if image:
            article.image = image
            
        article.title = title
        article.content = content
        
        article.save()
        return redirect('articles:detail', article_pk)

    # GET으로 들어왔을 때에는 update를 하기 위한 FORM을 제공하는 페이지를 주자.
    else:
        context = {
            "article" : article,
        }
        return  render(request, 'articles/update.html', context)


    # context = {
    #     'title' : aritcle.title,
    #     'content' : aritcle.content,
    # }



def comments_create(request, article_pk):
    # article_pk에 해당하는 새로운 커멘트 생성...만 하는 view함수임
    # 생성한 다음 detail page로 redirect하면 된다.
    # article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        content = request.POST.get('content')
        comment = Comment()
        # comment.article = article # 어떤 article의 comment 인지 알려주기 위한 작업
        comment.article_id = article_pk  # 그렇기 따문에 이렇게 하는게 더 명확하다.
        comment.content = content
        comment.save()
        
    return redirect('articles:detail',article_pk)

def comments_delete(request, article_pk, comment_pk):
    # comment_pk 에 해당 댓글 삭제
    # 댓글 삭제 후 detail 페이지로 이동.
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_pk)
        # 404 페이지가 안뜬다는것은 있다는 뜻이니까. 바로 삭제
        comment.delete()
    return redirect('articles:detail', article_pk)
