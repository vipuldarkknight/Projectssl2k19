
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from . models import Question_Banks_Main, Questions_Main, created_paper, Question_Module, SubQuestions
from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm, CountryForm, QuestionBankRenameForm, QuestionModuleForm, SubQuestionForm
from configparser import ConfigParser 
# from . models import Question_Banks_Main, Questions_Main
# from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm
from .filters import QuestionsFilter, SubQuestionsFilter
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf

# Create your views here.
def qbList(request):
    qb_list = Question_Banks_Main.objects.filter(username=request.user.username).values('name').distinct()
    return render(request, 'home.html', {
        'qb_list': qb_list
    })

def your_paper(request):
    paper_list = created_paper.objects.filter(username=request.user.username)
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

        repeated = False
        temp = created_paper.objects.filter(username = request.user.username)

        for i in temp:
            if i.name == qp_name:
                repeated=True

        if len(qlist)!=0 and repeated==False:
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
    ques_module_list = Question_Module.objects.filter(username=request.user.username, qb_name=name)
    filter=QuestionsFilter(request.GET,queryset=ques_list)
    return render(request, 'detail_qb.html', {
        'filter':filter,
        'qb_detail_list': qb_detail_list,
        'ques_list': ques_list,
        'qb_name': name,
        'ques_module_list': ques_module_list
    })
def view_ques(request,id):
    ques=Questions_Main.objects.filter(id=id).get()
    return render (request, 'view_ques.html',{'ques':ques,'id':id})   
    

def view_ans(request,id):
    ques=Questions_Main.objects.filter(id=id).get()
    return render (request, 'view_ans.html',{'ques':ques,'id':id})

ques_form_list = []

def upload_qbfile(request, name):
    if request.method == 'POST':
        form = QuestionBankForm2(request.POST, request.FILES)
        if form.is_valid():
            qb = form.save(commit=False)
            qb.username = request.user.username
            qb.name = name
            qb.save()
            l=qsplit(qb.file)
            global ques_form_list
            ques_form_list = []

            for x in l:
                ques_l = Questions_Main()
                if 'statement' in x.keys():
                    ques_l.statement = x['statement']
                if 'answer' in x.keys():
                    ques_l.answer = x['answer']
                if 'marks' in x.keys():
                    ques_l.marks = x['marks']
                if 'difficulty' in x.keys():
                    ques_l.difficulty = x['difficulty']
                if 'tag' in x.keys():
                    ques_l.tag = x['tag']

                # ques_l.username = request.user.username
                # ques_l.qb_name = name

                form = QuestionForm(instance=ques_l)
                ques_form_list.append(form)

            return redirect('Home:add_ques_by_file',name = name)

    else:
        form = QuestionBankForm2()

    return render(request, 'add_qbfile.html', {
        'form': form
    })

def add_ques_by_file(request, name):
    global ques_form_list
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.username = request.user.username
            ques.qb_name = name
            ques.save()

            return redirect('Home:add_ques_by_file',name = name)

    else:

        if len(ques_form_list) > 0:

            form = ques_form_list[0]
            ques_form_list = ques_form_list[1:]

            return render(request, 'add_ques_by_file.html', {
                'form': form
            })

    return redirect('Home:detail_qb', name=name)


def delete_qb(request, name):
    Question_Banks_Main.objects.filter(name=name).delete()
    return redirect('Home:qbList')

def paper_detail(request, name):
    paper_instance = created_paper.objects.filter(username=request.user.username, name=name).get()
    ques_id_list = paper_instance.ques_id.split()
    ques_list = Questions_Main.objects.filter(pk__in=ques_id_list)

    filter=QuestionsFilter(request.GET,queryset=ques_list)
    return render(request, 'paper_detail.html', {
        'filter':filter,
        'ques_list': ques_list,
        'paper': paper_instance
    })

no_of_subquestions=0

def add_ques_module(request, name):
    if request.method == 'POST':
        form = QuestionModuleForm(request.POST)
        if form.is_valid():
            ques_module = form.save(commit=False)
            ques_module.username = request.user.username
            ques_module.qb_name = name
            ques_module.ques_id_string = ""
            ques_module.marks=0
            ques_module.save()

            global no_of_subquestions
            no_of_subquestions = ques_module.subquestions

            return redirect('Home:add_subques', id=ques_module.id)
            # return HttpResponse(name)

    else:
        form = QuestionModuleForm()

    return render(request, 'add_ques_module.html', {
        'form': form
    })

def add_subques(request, id):

    global no_of_subquestions
    ques_module = Question_Module.objects.get(id=id)

    if request.method == 'POST':
        form = SubQuestionForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.question_module_id = id
            ques.save()

            print(ques.marks)
            ques_module.marks = ques_module.marks + ques.marks
            ques_module.ques_id_string = ques_module.ques_id_string + str(ques.id) + " "
            ques_module.save()
            return redirect('Home:add_subques', id=id)
            # return HttpResponse(name)

    else:

        if no_of_subquestions > 0:

            no_of_subquestions = no_of_subquestions -1
            form = SubQuestionForm()

            return render(request, 'add_ques_manually.html', {
                'form':form
            })

    name = ques_module.qb_name
    return redirect('Home:detail_qb', name=name)

def ques_module_detail(request, id):
    ques_list = SubQuestions.objects.filter(question_module_id=id)
    filter=SubQuestionsFilter(request.GET,queryset=ques_list)
    ques_module = Question_Module.objects.get(id=id)
    name = ques_module.qb_name
    return render(request, 'ques_module_detail.html', {
        'filter':filter,
        'ques_list': ques_list,
        'qb_name': name,
        'ques_module': ques_module
    })


def view_subques(request, id):
    ques = SubQuestions.objects.filter(id=id).get()
    return render(request, 'view_ques.html', {'ques': ques, 'id': id})


def view_subans(request, id):
    ques = SubQuestions.objects.filter(id=id).get()
    return render(request, 'view_ans.html', {'ques': ques, 'id': id})

def edit_subques(request, id):
    ques_instance = SubQuestions.objects.get(id=id)

    if request.method == 'POST':
        form = SubQuestionForm(request.POST, instance=ques_instance)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.question_module_id = id
            ques.save()
            return redirect('Home:ques_module_detail', id=id)

    else:
        form = SubQuestionForm(instance=ques_instance)

        return render(request, 'add_ques_manually.html', {
            'form': form
        })


# def rename_qb(request, name):
#
#     this_qb = Question_Banks_Main.objects.filter(username=request.user.username, name=name)
#
#     if request.method == 'POST':
#         form = QuestionBankRenameForm(request.POST, instance=this_qb[0])
#         if form.is_valid():
#             qb = form.save(commit=False)
#             qb.username = request.user.username
#             # qb.save()
#
#             for i in this_qb:
#                 # print(qb.name)
#                 i.name = qb.name
#                 i.save()
#
#             return redirect('Home:qbList')
#     else:
#         form = QuestionBankForm(instance=this_qb[0])
#
#     return render(request, 'add_qb.html', {
#         'form': form
#     })


def qsplit(qfile):

    con=ConfigParser()
    path = "media/" + qfile.name
    con.read(path)
    sl=con.sections()
    ql=[]
    for s in sl:
        dic={}
        for op in con.options(s):
            dic[op]=con.get(s,op)
        ql=ql+[dic]
    return ql

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('quiz_template.html', data)
        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not found")    