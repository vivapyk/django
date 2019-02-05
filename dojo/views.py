from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
import os
# Create your views here.
from django.views.generic import DetailView

from dojo.forms import PostForm
from dojo.models import Post


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>장고만세</p>
        '''.format(name=name))


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html',
                  {
                      'form': form,
                  })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # post = Post(title=form.cleaned_data['title'],
            #             content = form.cleaned_data['content'])
            # post.save()

            # post= Post.objects.create(title=form.cleaned_data['title'],
            #                             content=form.cleaned_data['content'])
            #post.save

            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',
    {
        'form': form,
    })


def post_list2(request):
    name = '박영근'
    return render(request, 'dojo/post_list.html',{'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬 그리고 장고',
        'items':['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})

# def excel_download(request):
#     filepath - os.path.join(settings.BASE_DIR, '')
#     filename = os.path.basename(filepath)
#     with open(filepath, 'rb') as f:
#         response = HttpResponse(f, content_type= 'application/vnd.ms-excel')
#         response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
#         return response


post_detail = DetailView.as_view(model=Post)

