from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


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

    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'blog/post_list.html', context)
    # 'blog/post_list.html'템플릿 파일을 이용해 http 프로토콜로 응답


def post_detail(request, pk):
    # 확인
    # return HttpResponse(pk)
    """
    localhost:8000 /detail/로 온 요청을
    'blog/post_detail.html'을 render 한 결과를 리턴

    :param request:
    :return:
    """
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    # localhost:8000/add 접근시 뷰
    if request.method == 'POST':
        # 요청의 method가 POST일때
        # 데이터에 추가 및 삭제
        # HttpResponse로 POST요청에 담겨온
        # title과 content를 합친 문자열 데이터를 보여줌
        title = request.POST['title']
        content = request.POST['content']
        # ORM 을 사용해서 title과 content에 해당하는 Post생성
        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
        )
        # post-detail이라는 url name을 가진 뷰로 리다이렉션 요청 보냄
        # 이때, post-detail url name으로 특정 url 을 만드려면
        # pk 값이 필요하므로 키워드 인수로 해당 값을 넘겨준다.
        return redirect('post-detail', pk=post.pk)
    else:
        # 요청의 Method가 GET일때
        # 데이터를 보여주면됨
        return redirect(request, 'blog/post_add.html', {})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post-list')
