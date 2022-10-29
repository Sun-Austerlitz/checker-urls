import requests
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from .models import Url


@login_required
def dashboard(request):
    object_list = Url.objects.filter(author=request.user.id)
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        urls = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        urls = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        urls = paginator.page(paginator.num_pages)
    return render(request, 'checking/dashboard.html', {'page': page, 'urls': urls})


def checker(request):
    if request.method == 'GET':
        try:
            url = Url.objects.get(id=request.GET.get('pk'))
            r = requests.get(url)
            url.status_code = r.status_code
            url.save()
            return HttpResponse(r.status_code)
        except requests.exceptions.RequestException as e:
            url.status_code = None
            url.save()
            return HttpResponse('')


def get_last_update(request):
    if request.method == 'GET':
        try:
            return HttpResponse(Url.objects.get(id=request.GET.get('pk')).updated.strftime("%Y-%m-%d %H:%M:%S"))
        except requests.exceptions.RequestException as e:
            return HttpResponse(e.errno)



