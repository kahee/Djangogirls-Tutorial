from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_list(request):
    # 브라우저에서 요청 (localhost:8000 입력)/ 0.0.0.0:8000 외부에서 접근 가능
    # 요청 runserver로 실행중인 서버에 도착
    # runserver 요청을 django code로 전달
    # Django code 중 config.urls 모듈이 해당 요청을 받음
    # config.urls 모듈은 ''(/admin/를 제외한 모든 요청)을 blog.urls 모듈로 전달
    # blog.urls모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 있다면 일치하는 패턴과 연결된 함수 (view)를 실행
    #   7.1 settings 모듈의 TEMPLATES속성 내의 DIRS목록에서 blog/post_list.html 파일의 내용을 가져옴
    #   7.2 가져온 내용을 적절히 처리(렌더링, render()함수))하여 리턴
    # 함수의 실행 결과를 브러우저로 다시 전달

    # HTTP 프로토콜로 텍스트 데이터 응답
    # return HttpResponse('<html>~')

    # 'blog/post_list.html'템플릿 파일을 이용해 http 프로토콜로 응답
   return render(request, 'blog/post_list.html')
