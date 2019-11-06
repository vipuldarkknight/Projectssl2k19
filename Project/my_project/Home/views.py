from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from . models import Question_Banks_Main
from .forms import QuestionBankForm, QuestionBankForm2

# Create your views here.
def qbList(request):
    qb_list = Question_Banks_Main.objects.filter(username=request.user.username).values('name').distinct()
    return render(request, 'home.html', {
        'qb_list': qb_list
    })

def add_qb(request):
    if request.method == 'POST':
        form = QuestionBankForm(request.POST, request.FILES)
        if form.is_valid():
            qb = form.save(commit=False)
            qb.username = request.user.username
            qb.save()
            return redirect('Home:qbList')
    else:
        form = QuestionBankForm()

    return render(request, 'add_qb.html', {
        'form': form
    })

def detail_qb(request, name):
    qb_detail_list = Question_Banks_Main.objects.filter(username=request.user.username, name=name)
    return render(request, 'detail_qb.html', {
        'qb_detail_list': qb_detail_list,
        'qb_name': name
    })

def upload_qbfile(request, name):
    if request.method == 'POST':
        form = QuestionBankForm2(request.POST, request.FILES)
        if form.is_valid():
            qb = form.save(commit=False)
            qb.username = request.user.username
            qb.name = name
            qb.save()
            # base_url = reverse('detail_qb')
            # url = '{}?{}'.format(base_url, name)
            # return redirect(url)
            return redirect('Home:detail_qb',name = name)
            # return HttpResponse(name)
            # return redirect('qbList')
    else:
        form = QuestionBankForm2()

    return render(request, 'add_qb.html', {
        'form': form
    })

    # return HttpResponse(name)
