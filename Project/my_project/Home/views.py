
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.template import RequestContext

from . models import Question_Banks_Main, Questions_Main, created_paper
from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm, CountryForm, SingleCorrectForm, MCQForm
from django.forms import formset_factory
# from django.shortcuts import render
# from myapp.forms import ArticleForm

from configparser import ConfigParser 
# from . models import Question_Banks_Main, Questions_Main
# from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm
from .filters import QuestionsFilter
# Create your views here.

def SingleCorrectMCQ(request, name):
    ArticleFormSet = formset_factory(SingleCorrectForm, extra=2, max_num=1)
    BookFormSet = formset_factory(MCQForm)
    if request.method == 'POST':
        article_formset = ArticleFormSet(request.POST, request.FILES, prefix='articles')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if article_formset.is_valid() and book_formset.is_valid():
            # do something with the cleaned_data on the formsets.
            pass
    else:
        article_formset = ArticleFormSet(prefix='articles')
        book_formset = BookFormSet(prefix='books')
    return render(request, 'single_correct.html', {
        'article_formset': article_formset,
        'book_formset': book_formset,
    })


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
        form = QuestionForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.username = request.user.username
            ques.qb_name = name
            ques.save()
            return redirect('Home:detail_qb', name=name)
            # return HttpResponse(name)

    else:
        form = QuestionForm()

    return render(request, 'add_ques_manually.html', {
        'form': form
    })

def edit_ques(request, id):
    ques_instance = Questions_Main.objects.get(id=id)

    name = ques_instance.qb_name

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=ques_instance)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.username = request.user.username
            ques.qb_name = name
            ques.save()
            return redirect('Home:detail_qb', name=name)

    else:
        form = QuestionForm(instance=ques_instance)

        return render(request, 'add_ques_manually.html', {
            'form': form
        })


def detail_qb(request, name):
    qb_detail_list = Question_Banks_Main.objects.filter(username=request.user.username, name=name)[1:]
    ques_list = Questions_Main.objects.filter(username=request.user.username, qb_name=name)
    filter=QuestionsFilter(request.GET,queryset=ques_list)
    return render(request, 'detail_qb.html', {
        'filter':filter,
        'qb_detail_list': qb_detail_list,
        'ques_list': ques_list,
        'qb_name': name
    })
def view_ques(request,id):
    ques=Questions_Main.objects.filter(id=id).get()
    return render (request, 'view_ques.html',{'ques':ques,'id':id})   
    

def view_ans(request,id):
    ques=Questions_Main.objects.filter(id=id).get()
    return render (request, 'view_ans.html',{'ques':ques,'id':id})  
    
def upload_qbfile(request, name):
    if request.method == 'POST':
        form = QuestionBankForm2(request.POST, request.FILES)
        if form.is_valid():
            qb = form.save(commit=False)
            qb.username = request.user.username
            qb.name = name
            qb.save()
            l=qsplit(qb.file)
            
            for x in l:
                ques_l = Questions_Main()
                if statement in x.keys():
                    ques_l.statement = x[statement]
                if answer in x.keys():
                    ques_l.answer = x[answer]
                if marks in x.keys():
                    ques_l.marks = x[marks]
                if difficulty in x.keys():
                    ques_l.difficulty = x[difficulty]
                if tag in x.keys():
                    ques_l.tag = x[tag]
            # base_url = reverse('detail_qb')
            # url = '{}?{}'.format(base_url, name)
            # return redirect(url)
            # return redirect('Home:detail_qb',name = name)
            # return HttpResponse(name)
            # return redirect('qbList')
            
            form = QuestionForm(instance=ques_instance)
    else:
        form = QuestionBankForm2()

    return render(request, 'add_qbfile.html', {
        'form': form
    })


def delete_qb(request, name):
    Question_Banks_Main.objects.filter(name=name).delete()
    return redirect('Home:qbList')

# def countries_view(request):
#     if request.method == 'POST':
#         form = CountryForm(request.POST)
#         if form.is_valid():
#             countries = form.cleaned_data.get('countries')
#             # do something with your results
#     else:
#         form = CountryForm

#     return render_to_response('add_paper.html', {'form': form},
#                               context_instance=RequestContext(request))

def qsplit(qfile):
    con=ConfigParser()
    con.read(qfile)
    sl=con.sections()
    ql=[]
    for s in sl:
        dic={}
        for op in con.options(s):
            dic[op]=con.get(s,op)
        ql=ql+[dic]    
    return ql        
    
