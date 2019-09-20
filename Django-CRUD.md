# Django-CRUD



DB생성하기 (Django-Crud 이전파일 참조)



# 1. 웹 생성하기(복습)

step

1.  urls.py에 path 설정

   - project-> app->urls순으로 이동해야 함

   crud(project 이름)/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('articles/', include(articles.urls)),
       path('admin/', admin.site.urls),
   ]
   ```

   위와같이 설정하고, articles/urls.py 파일을 생성 한 뒤 다음과 같이 작성한다.

   참고로 path명령은 django.urls모듈이 가지고 있으므로 임포트 한다.

   ```
   
   ```

   

2. views.py에 함수 설정

3. templates에서 html파일 생성



# 2. URL에 이름을 지어주기

1. urls.py에 path들의 이름을 붙여준다.

```python
urlpatterns = [
    path('', views.index, name='index'),#3 맨 처음페이지에 우리의 db를 보여주는 페이지를 만들어보자
   
    path('<int:article_pk>', views.detatil, name='detail'),  #4 인덱스에서 보여주는 게시글의 디테일을 보여주는 페이지를 만든다.
    
    path('new/', views.new, name='new'),  # 1입력 페이지 생성
    path('create/', views.create, name='create'),  # 2데이터를 전달받아 데이터를 저장.
    # 매핑 - url에 create라는 입력을 받으면, view.py에 있는 create라는 함수를 실행해줘!

    path('<int:article_pk>/delete/', views.delete, name='delete'),  # 5 삭제기능만들기
]
```

2. views.py에 redirect를 수정한다.

```python
def create(request):

    # articles/new/를 통해 new.html의 form에서 전달받은 데이터 
    title = request.GET.get('title')
    content = request.GET.get('content')

    #우리가 받은 데이터를 DB에 생성하자
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('detail', article.pk )

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('index')
    
```

- 기존의 redirect주소는 하드코딩 되어있던 주소였지만 naming하고 난 뒤에는 variavle Routing을 제외한 이름을 선언하고, 뒤에 ,로 구분한 뒤 variable routing인자를 CRUD로 받은 객체의 pk값으로 지정한다.



3. 모든 html 파일에서 연결되어 있는 a태그를 수정한다.

   ex)index.html

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>index</title>
   </head>
   <body>
     <h1>Articles</h1>
   
     <a href="{% url 'new' %}">[작성하기]</a>
     <hr>
     {% for article in articles  %}
     <div>
       <a href="{% url 'detail' article.pk %}"><h3>{{ article.pk }}. {{ article.title }}</h3></a>
       
       <p>{{ article.content }}</p>
     </div>
     <br>
     {% endfor %}
   </body>
   </html>
   ```

   - a태그 안에서 url + tap 하고 '이름'을 작성하면 된다. 만약 variable routing을 사용한 주소가 있다면, '이름' 뒤에 콤마하고 variable routing의 어트리뷰트 이름을 써준다.

     

4.  만약 여러 어플리케이션이 모아져 있는 프로젝트를 관리하고 있다면, templates를 관리하여 다른 application에 있는 같은 이름의 html을 구분하기 위해 명시적으로 `articles/index.html/`로 관리하듯이 `app_name= 'articles'`로 app이름을 명시적으로 작성하여 각각의 url name을 구분하도록 한다.

   - urls.py 에 app_name 선언하기

     ```python
     from django.urls import path
     from. import views
     # /articles/__
     app_name = 'articles'
     urlpatterns = [
         path('', views.index, name='index'),#3 맨 처음페이지에 우리의 db를 보여주는 페이지를 만들어보자
        
         path('<int:article_pk>', views.detatil, name='detail'),  #4 인덱스에서 보여주는 게시글의 디테일을 보여주는 페이지를 만든다.
         
         path('new/', views.new, name='new'),  # 1입력 페이지 생성
         path('create/', views.create, name='create'),  # 2데이터를 전달받아 데이터를 저장.
         # 매핑 - url에 create라는 입력을 받으면, view.py에 있는 create라는 함수를 실행해줘!
     
         path('<int:article_pk>/delete/', views.delete, name='delete'),  # 5 삭제기능만들기
     ]
     ```

   - views.py 와 각각의 html에 명시적으로 구분하는 작업 하기

     ex)     `return redirect('articles:index')`

     ```python
     def delete(request, article_pk):
         article = Article.objects.get(pk=article_pk)
         article.delete()
         return redirect('articles:index')
     ```

     

# 3 BASE Templates 생성하기(복습)

1. crud/settings.py

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   
   ```

   - `APP_DIRS : True` 이기 때문에 app 안에 있는 templates를 읽을 수 있는 것이다.

2. crud/templates 생성

3. crud/settings.py/templates 에서

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           
           
           'DIRS': [], # 이 아이를 수정해야 한다.
           
           
           
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   ```python
           'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
   		# 다음과 같이 설정한다.
   ```

4. crud/templates/base.html

   ```django
   <!DOCTYPE html>
   <html lang="ko">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>
       {% block title %}
       {% endblock title %}
     </title>
   </head>
   <body>
     {% block body %}
     {% endblock body %}
   </body>
   </html>
   ```

   블럭을 생성하여 쉽게 사용할 수 있도록 설정한다.

   

5. app/<이름>.html 수정하기

   ex)index.html

   ```django
   {% extends 'base.html' %}
   
   {% block title %}
     index
   {% endblock title %}
   
   {% block body %}
     <h1>Articles</h1>
   
       <a href="{% url 'articles:new' %}">[작성하기]</a>
       <hr>
       {% for article in articles  %}
       <div>
         <a href="{% url 'articles:detail' article.pk %}"><h3>{{ article.pk }}. {{ article.title }}</h3></a>
         
         <p>{{ article.content }}</p>
       </div>
       <br>
       {% endfor %}
   
   {% endblock body %}
   
   ```

   

# 4. REST API

참고자료 : https://meetup.toast.com/posts/92



​    \# 만약 GET요청으로 들어오면 html 페이지 rendering

​    \# 아니라면(POST 라면) 사용자 데이터를 받아서 articles 생성

```python
# def new 삭제하고 create와 하나로 합친다.

def create(request):
    # 만약 GET요청으로 들어오면 html 페이지 rendering
    if request.method == 'GET':
        return render(request,'articles/new.html')
    
    # 아니라면(POST 라면) 사용자 데이터를 받아서 articles 생성
    else:

        # articles/new/를 통해 new.html의 form에서 전달받은 데이터 
        title = request.GET.get('title')
        content = request.GET.get('content')

        #우리가 받은 데이터를 DB에 생성하자
        article = Article()
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)

```



이슈 CSRF 토큰 넣기 	



# 5. django_extensions

1. 인스톨하기

```bash
$ pip install django_extensions
```

2. <project>/settings.py에 등록하기  # 서트파티 앱 등록

```python
INSTALLED_APPS = [
    #Local app
    'articles',
    'jobs',

    # third party apps
    'django_extensions',

```

3. bash에서 

```bash
python manage.py shell_plus
```

4.  기존에 Article에 데이터 삽입

```python
article = Article()
article.title = '새로운 데ㅣ터 헤헤헤헤'
aritcle.content = '새로운 내용이 들ㅇ왔어요'

article.save()

comment = Comment()
comment.content = '첫번째 댓글'
comment.article = article
comment.save()

comment = Comment(article=article, content='두번째 댓굴이에오')
comment.save()
```

5. article 이 사용할 수 있는 모든 명령어들

```python
dir(article)

['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', '_check_id_field',
'_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'clean', 'clean_fields', 
 
 'comment_set', 
 
 'content', 'created_at', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_deferred_fields', 'get_next_by_created_at', 'get_next_by_updated_at', 'get_previous_by_created_at', 'get_previous_by_updated_at', 'id', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'title', 'unique_error_message', 'updated_at', 'validate_unique']

```



```python
 dir(article.comment_set)

['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_apply_rel_filters', '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_remove_prefetched_objects', '_set_creation_counter', '_update', 'add', 'aggregate',
 
 'all', 
 
 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'core_filters', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'do_not_call_in_templates', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'field', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_prefetch_queryset', 'get_queryset', 'in_bulk', 'instance', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'set', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']
```

 ```python
pip install ipython  # 좀더 사용자에게 편한 출력데이터 제공
 ```



6. comments = article.comment_set.all()

```python
In [4]: comments
Out[4]: <QuerySet [<Comment: 두번째 댓굴이에오>]>
```



 # 6. 게시판에 댓글 창 만들기

### 1) 댓글 창 보여주기

1. views.py/detail함수

```python

# 꼭 클래스를 임포트 할 것
from .models import Article, Comment


# variable roution 으로 사용자가 보기를 원하는 페이지 pk를 받아서 디페일 페이지에 보여준다.
def detatil(request, article_pk):
    # SELECT * FROM articles WHERE pk=article_pk
    article = get_object_or_404(Article,pk=article_pk)

    # article에 대한 모든 댓글을 꺼내겠다.
    comments = article.comment_set.all()


    context = {
        'article' : article,
        'comments' : comments
    }
    return render(request, 'articles/detail.html', context)
```

2. detail.html

```html
<h4>댓글</h4>
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="text", name='content'>
      <button type="submit">댓글달기</button>
    </form>
```

- 댓글입력창 작성, action에는 우리가 생성한 comments_create view.py에 접근하라고 보낸다.

- views.py에서`def comments_create(request, article_pk):`는 article_pk에 해당하는 새로운 커멘트를 생성하는 함수이다.

2.2 detail.html

```python
 <ul>
  {% for comment in comments %}
    <li>{{ comment.content }}</li>
  {% empty %}
    <p>아직 댓글이 없습니다.</p>
  {% endfor %}
  </ul>
```

- detail함수에서 comments를 정의했기 때문에, 다음과 같이 출력할 수 있다. 만약 댓글이 없다면,  empty문이 출력되고, 댓글이 있다면 포문안에서 출력이 된다.



3. view.py

```python
def comments_create(request, article_pk):
    # article_pk에 해당하는 새로운 커멘트 생성...만 하는 view함수임
    # 생성한 다음 detail page로 redirect하면 된다.
    # article = get_object_or_404(Article,pk=article_pk)
    if request.method == "POST":
        content = request.POST.get('content')
        comment = Comment()
        # comment.article = article
        comment.article_id = article_pk
        comment.content = content
        comment.save()
        
    return redirect('articles:detail',article_pk)


```

- 관계를 나타내는 column이름은 자동으로 생성 (연결되어있는 클래스 이름이 article이기 때문에 article_id라는 이름의 column이 생성되고, foreign key로 관리 된다.)

- foeign key 연결은 두가지 방법이 가능하다. 

  - ` comment.article_id = article_pk`
  - `article = get_object_or_404(Article,pk=article_pk)` , `comment.article = article`

  