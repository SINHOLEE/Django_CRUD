from django.urls import path
from. import views
# /articles/__
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),#3 맨 처음페이지에 우리의 db를 보여주는 페이지를 만들어보자    
    # path('new/', views.new, name='new'),  # 1입력 페이지 생성 #6 REST API형식으로 가기 위해 CREATE만 남긴다.
    path('create/', views.create, name='create'),  # 2데이터를 전달받아 데이터를 저장.
    # 매핑 - url에 create라는 입력을 받으면, view.py에 있는 create라는 함수를 실행해줘!

    path('<int:article_pk>/update/', views.update, name='update'),

    path('<int:article_pk>', views.detatil, name='detail'),  #4 인덱스에서 보여주는 게시글의 디테일을 보여주는 페이지를 만든다.
    path('<int:article_pk>/delete/', views.delete, name='delete'),  # 5 삭제기능만들기
    

    path('<int:article_pk>/comments/', views.comments_create, name='comments_create')  # 6 댓글을 관리하는 url만들기
]