from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from configparser import ConfigParser 
from . models import Question_Banks_Main, Questions_Main
from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm

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
            # l=qsplit(qb.file)
            # ques_form_list = []

            # file = Question_Banks_Main.objects.last().file
            # l = qsplit(file)

            # print(file.name)
            # print(l)

            # for filename, file in request.FILES.items():
            #     name2 = request.FILES[filename]
                # l=qsplit(file)

            # con = ConfigParser()
            # print(con)
            # print(con.read(name2))
            # sl = con.sections()
            # print(name2)
            # ql = []
            # for s in sl:
            #     dic = {}
            #     for op in con.options(s):
            #         dic[op] = con.get(s, op)
            #     ql = ql + [dic]
            #
            # print(len(ql))
            #
            # return HttpResponse(name2)

            # return HttpResponse(len(l))
            # print(file.name.url)

            # with open(Question_Banks_Main.objects.get(id=16).file, 'wb+') as x:
            # doc = request.FILES
            # return HttpResponse(len(l))
            # r = requests.get(“/media/try.ini”)

            # for x in l:
            #     ques_l = Questions_Main()
            #     if 'statement' in x.keys():
            #         ques_l.statement = x['statement']
            #     if 'answer' in x.keys():
            #         ques_l.answer = x['answer']
            #     if 'marks' in x.keys():
            #         ques_l.marks = x['marks']
            #     if 'difficulty' in x.keys():
            #         ques_l.difficulty = x['difficulty']
            #     if 'tag' in x.keys():
            #         ques_l.tag = x['tag']
            #
            #     form = QuestionForm(instance=ques_l)
            #     ques_form_list.append(form)
            # base_url = reverse('detail_qb')
            # url = '{}?{}'.format(base_url, name)
            # return redirect(url)

            # return add_ques_by_file(request, ques_form_list, name)

            return redirect('Home:detail_qb',name = name)
            # return redirect('Home:add_ques_by_file',name = name)
            # return HttpResponse(len(ques_form_list))
            # return redirect('qbList')

            # return render(request, 'add_ques_by_file.html', {
            #     'qb_name': name,
            #     'ques_form_list': ques_form_list
            # })

    else:
        form = QuestionBankForm2()

    return render(request, 'add_qbfile.html', {
        'form': form
    })

def add_ques_by_file(request, name):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.username = request.user.username
            ques.qb_name = name
            ques.save()

            # if len(ques_form_list) != 0:
            #     return redirect('Home:detail_qb', name=name)
            # else:
            #     add_ques_by_file(request, ques_form_list[1:], name)
            return HttpResponse(name)

    else:
        form = QuestionForm()

    return render(request, 'add_ques_manually.html', {
        'form': form
    })


def delete_qb(request, name):
    Question_Banks_Main.objects.filter(name=name).delete()
    return redirect('Home:qbList')

def qsplit(qfile):

    con=ConfigParser()
    # print(qfile.name)
    path = "media/" + qfile.name
    print(con.read(path))
    sl=con.sections()
    print(qfile)
    ql=[]
    for s in sl:
        dic={}
        for op in con.options(s):
            dic[op]=con.get(s,op)
        ql=ql+[dic]
    return ql