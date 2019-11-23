
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.template import RequestContext

from . models import Question_Banks_Main, Questions_Main, created_paper
from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm, CountryForm

# Create your views here.
def qbList(request):
    qb_list = Question_Banks_Main.objects.filter(username=request.user.username).values('name').distinct()
    return render(request, 'home.html', {
        'qb_list': qb_list
    })

def your_paper(request):
    paper_list = created_paper.objects.filter(username=request.user.username).values('name').distinct()
    return render(request, 'see_ques.html', {
        'paper_list': paper_list
    })

def add_paper(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        qlist = request.POST.getlist('Question_List')
        qp_name = request.POST.get('QP_name')
        # if form.is_valid():
            # qpaper = form.save(commit=False)
            # qpaper.username = request.user.username
            # qpaper.save()
        # print(qlist)
        # print(request.POST.get('QP_name'))
        if len(qlist)!=0:
            qp = created_paper()
            qp.name = qp_name
            qp.username = request.user.username
            qp.num_ques = len(qlist)

            ids = ""
            marks_sum = 0

            for i in qlist:
                id_temp = i[0]
                ids = ids + id_temp + " "
                ques_temp = Questions_Main.objects.filter(id=id_temp).get()
                marks_sum = marks_sum + ques_temp.marks

            qp.marks = marks_sum
            qp.ques_id = ids
            qp.save()

        return redirect('Home:your_paper')
    else:
        form = CountryForm()
        q_list = Questions_Main.objects.filter(username=request.user.username)
        # print(q_list)
        q_tup = []
        for i in q_list:
            x=[i.id,i.tag]
            x=tuple(x)
            q_tup.append(x)
        q_tup = tuple(q_tup)
        # print(request.user.username)
        form.fields["Question_List"].choices = q_tup

    return render(request, 'add_paper.html', {
        'form': form
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

def add_ques_manually(request, name):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.username = request.user.username
            ques.qb_name = name
            ques.marks=3
            ques.save()
            return redirect('Home:detail_qb', name=name)
            # return HttpResponse(name)

    else:
        form = QuestionForm()

    return render(request, 'add_ques_manually.html', {
        'form': form
    })

def detail_qb(request, name):
    qb_detail_list = Question_Banks_Main.objects.filter(username=request.user.username, name=name)[1:]
    ques_list = Questions_Main.objects.filter(username=request.user.username, qb_name=name)
    return render(request, 'detail_qb.html', {
        'qb_detail_list': qb_detail_list,
        'ques_list': ques_list,
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

    return render(request, 'add_qbfile.html', {
        'form': form
    })


def delete_qb(request, name):
    Question_Banks_Main.objects.filter(name=name).delete()
    return redirect('Home:qbList')

def countries_view(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            countries = form.cleaned_data.get('countries')
            # do something with your results
    else:
        form = CountryForm

    return render_to_response('add_paper.html', {'form': form},
                              context_instance=RequestContext(request))

