from itertools import chain

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.template.loader import get_template
# from . models import Question_Banks_Main, Questions_Main, created_paper
# from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm, CountryForm, SingleCorrectForm, MCQForm
from django.forms import formset_factory
# from django.shortcuts import render
# from myapp.forms import ArticleForm
from . models import Question_Banks_Main, Questions_Main, created_paper, Question_Module, SubQuestions
from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm, CountryForm, QuestionBankRenameForm, QuestionModuleForm, SubQuestionForm, SingleCorrectForm, MCQForm, MultiCorrectForm, MatchtheColumnForm, MatchtheColumn2Form

from configparser import ConfigParser 
# from . models import Question_Banks_Main, Questions_Main
# from .forms import QuestionBankForm, QuestionBankForm2, QuestionForm
from .filters import QuestionsFilter, SubQuestionsFilter
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
import os
from django.contrib import messages

# Create your views here.

@login_required
def SingleCorrectMCQ(request, name):
    ArticleFormSet = formset_factory(SingleCorrectForm, extra=2, max_num=1)
    BookFormSet = formset_factory(MCQForm)
    if request.method == 'POST':
        article_formset = ArticleFormSet(request.POST, request.FILES, prefix='articles')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if article_formset.is_valid() and book_formset.is_valid():
            # do something with the cleaned_data on the formsets.

            for data in book_formset.cleaned_data:
                
                qstatement = data['statement']
                qmarks = data['marks']
                qdifficulty = data['difficulty']
                qtag = data['tag']

                statement_final = ""
                statement_final = statement_final + qstatement + "\n"

            for data in article_formset.cleaned_data:

                statement_final = statement_final + "A) " + data['Choice1'] + "\n"
                statement_final = statement_final + "B) " + data['Choice2'] + "\n"
                statement_final = statement_final + "C) " + data['Choice3'] + "\n"
                statement_final = statement_final + "D) " + data['Choice4'] + "\n"

                qans = data['Answer']

            q = Questions_Main()
            q.statement=statement_final
            q.marks=qmarks
            q.difficulty=qdifficulty
            q.tag=qtag
            q.answer=qans
            q.qtype=2
            q.username=request.user.username
            q.qb_name=name
            q.save()

            return redirect('Home:detail_qb', name=name)            
    else:
        article_formset = ArticleFormSet(prefix='articles')
        book_formset = BookFormSet(prefix='books')
    return render(request, 'single_correct.html', {
        'article_formset': article_formset,
        'book_formset': book_formset,
    })

@login_required
def MultiCorrectMCQ(request, name):
    ArticleFormSet = formset_factory(MultiCorrectForm, extra=2, max_num=1)
    BookFormSet = formset_factory(MCQForm)
    if request.method == 'POST':
        article_formset = ArticleFormSet(request.POST, request.FILES, prefix='articles')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if article_formset.is_valid() and book_formset.is_valid():
            
            for data in book_formset.cleaned_data:
                
                qstatement = data['statement']
                qmarks = data['marks']
                qdifficulty = data['difficulty']
                qtag = data['tag']

                statement_final = ""
                statement_final = statement_final + qstatement + "\n"

            for data in article_formset.cleaned_data:

                statement_final = statement_final + "A) " + data['Choice1'] + "\n"
                statement_final = statement_final + "B) " + data['Choice2'] + "\n"
                statement_final = statement_final + "C) " + data['Choice3'] + "\n"
                statement_final = statement_final + "D) " + data['Choice4'] + "\n"

                qans = data['Choose_Answers']
                qans_string = ""

                for a in qans:
                    qans_string = qans_string + a + "\n"

            q = Questions_Main()
            q.statement=statement_final
            q.marks=qmarks
            q.difficulty=qdifficulty
            q.tag=qtag
            q.answer=qans_string
            q.qtype=3
            q.username=request.user.username
            q.qb_name=name
            q.save()

            return redirect('Home:detail_qb', name=name)
    else:
        article_formset = ArticleFormSet(prefix='articles')
        book_formset = BookFormSet(prefix='books')
    return render(request, 'multi_correct.html', {
        'article_formset': article_formset,
        'book_formset': book_formset,
    })

@login_required
def matchthecolumns(request, name):
    ArticleFormSet = formset_factory(MatchtheColumnForm, extra=2, max_num=1)
    ArticleFormSet1 = formset_factory(MatchtheColumn2Form, extra=2, max_num=1)
    BookFormSet = formset_factory(MCQForm)
    if request.method == 'POST':
        article_formset = ArticleFormSet(request.POST, request.FILES, prefix='articles')
        article_formset1 = ArticleFormSet1(request.POST, request.FILES, prefix='articles1')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if article_formset.is_valid() and book_formset.is_valid() and article_formset1.is_valid():
            
            for data in book_formset.cleaned_data:
                
                qstatement = data['statement']
                qmarks = data['marks']
                qdifficulty = data['difficulty']
                qtag = data['tag']

                statement_final = ""
                statement_final = statement_final + qstatement + "\n"
        
            for data in article_formset.cleaned_data:

                statement_final = statement_final + "A) " + data['Choice1'] + "\n"
                statement_final = statement_final + "B) " + data['Choice2'] + "\n"
                statement_final = statement_final + "C) " + data['Choice3'] + "\n"
                statement_final = statement_final + "D) " + data['Choice4'] + "\n"

                qans1 = data['Answer1']
                qans2 = data['Answer2']
                qans3 = data['Answer3']
                qans4 = data['Answer4']

            for data in article_formset1.cleaned_data:

                statement_final = statement_final + "A) " + data['A'] + "\n"
                statement_final = statement_final + "B) " + data['B'] + "\n"
                statement_final = statement_final + "C) " + data['C'] + "\n"
                statement_final = statement_final + "D) " + data['D'] + "\n"


            qans_string=""
            qans_string = qans1 + "\n" + qans2 + "\n" + qans3 + "\n" + qans4 + "\n" 
            
            q = Questions_Main()
            q.statement=statement_final
            q.marks=qmarks
            q.difficulty=qdifficulty
            q.tag=qtag
            q.answer=qans_string
            q.qtype=4
            q.username=request.user.username
            q.qb_name=name
            q.save()

            return redirect('Home:detail_qb', name=name)


    else:
        article_formset1 = ArticleFormSet1(prefix='articles1')
        article_formset = ArticleFormSet(prefix='articles')
        book_formset = BookFormSet(prefix='books')
    return render(request, 'matchcolumns.html', {
        'article_formset': article_formset,
        'article_formset1': article_formset1,
        'book_formset': book_formset,
    })

def qbList(request):
    qb_list = Question_Banks_Main.objects.filter(username=request.user.username).values('name').distinct()
    return render(request, 'home.html', {
        'qb_list': qb_list
    })

@login_required
def your_paper(request):
    paper_list = created_paper.objects.filter(username=request.user.username)
    return render(request, 'see_ques.html', {
        'paper_list': paper_list
    })

@login_required
def add_paper(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        qlist = request.POST.getlist('Question_List')
        # print(qlist)
        qmlist = request.POST.getlist('Question_Module_List')
        qp_name = request.POST.get('QP_name')
        qp_duration = request.POST.get('Duration')
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

        if repeated==False:
            if len(qlist)!=0 or len(qmlist)!=0:
                qp = created_paper()
                qp.name = qp_name
                qp.username = request.user.username
                qp.num_ques = len(qlist)
                qp.num_ques_modules = len(qmlist)
                qp.duration = qp_duration

                ids = ""
                qm_ids=""
                marks_sum = 0

                for i in qlist:
                    id_temp = i
                    print(id_temp)
                    ids = ids + id_temp + " "
                    ques_temp = Questions_Main.objects.filter(id=id_temp).get()
                    marks_sum = marks_sum + ques_temp.marks

                for i in qmlist:
                    id_temp=i
                    qm_ids = qm_ids + id_temp + " "
                    ques_module_temp = Question_Module.objects.filter(id=id_temp).get()
                    marks_sum = marks_sum + ques_module_temp.marks

                qp.marks = marks_sum
                qp.total_sum_ques = len(qlist) + len(qmlist)
                qp.ques_id = ids
                qp.ques_module_id = qm_ids
                qp.save()

                return redirect('Home:your_paper')
            else:
                messages.add_message(request, messages.INFO, 'Questions cannot be empty')
                return redirect('Home:add_paper')
        else:
            messages.add_message(request, messages.INFO, 'Same Name Paper Already Exists')
            return redirect('Home:add_paper')
    else:
        form = CountryForm()
        q_list = Questions_Main.objects.filter(username=request.user.username)
        qm_list = Question_Module.objects.filter(username=request.user.username)
        # print(q_list)
        q_tup = []
        qm_tup=[]
        for i in q_list:
            x=[i.id,i.statement[:100]]
            x=tuple(x)
            q_tup.append(x)
        for i in qm_list:
            x=[i.id,i.statement]
            x=tuple(x)
            qm_tup.append(x)
        q_tup = tuple(q_tup)
        qm_tup = tuple(qm_tup)
        # print(request.user.username)
        form.fields["Question_List"].choices = q_tup
        form.fields["Question_Module_List"].choices = qm_tup

    return render(request, 'add_paper.html', {
        'form': form
    })

@login_required
def add_qb(request):
    if request.method == 'POST':
        form = QuestionBankForm(request.POST, request.FILES)
        qb_list = Question_Banks_Main.objects.filter(username=request.user.username)
        if form.is_valid():

            qb = form.save(commit=False)

            for x in qb_list:
                if qb.name == x.name:
                    messages.add_message(request, messages.INFO, 'Same Name Question Bank Already Exists')
                    return redirect('Home:add_qb')

            qb.username = request.user.username
            qb.save()
            return redirect('Home:qbList')
    else:
        form = QuestionBankForm()

    return render(request, 'add_qb.html', {
        'form': form
    })

@login_required
def add_ques(request, name):
    return render(request, 'add_ques.html', {
        'name': name
    })

@login_required
def add_ques_manually(request, name):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.username = request.user.username
            ques.qb_name = name
            ques.qtype = 1
            ques.save()
            return redirect('Home:detail_qb', name=name)
            # return HttpResponse(name)

    else:
        form = QuestionForm()

    return render(request, 'add_ques_manually.html', {
        'form': form
    })

@login_required
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

@login_required
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

@login_required
def view_ques(request,id):
    ques=Questions_Main.objects.filter(id=id).get()
    return render (request, 'view_ques.html',{'ques':ques,'id':id})   
    
@login_required
def view_ans(request,id):
    ques=Questions_Main.objects.filter(id=id).get()
    return render (request, 'view_ans.html',{'ques':ques,'id':id})

ques_form_list = []

@login_required
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

@login_required
def add_ques_by_file(request, name):
    global ques_form_list
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.username = request.user.username
            ques.qb_name = name
            ques.qtype = 1
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

@login_required
def delete_qb(request, name):
    Question_Banks_Main.objects.filter(name=name).delete()
    return redirect('Home:qbList')

@login_required
def paper_detail(request, name):
    paper_instance = created_paper.objects.filter(username=request.user.username, name=name).get()
    ques_id_list = paper_instance.ques_id.split()
    ques_list = Questions_Main.objects.filter(pk__in=ques_id_list)
    ques_module_id_list = paper_instance.ques_module_id.split()
    ques_module_list = Question_Module.objects.filter(pk__in=ques_module_id_list)
    print(paper_instance.ques_module_id)

    filter=QuestionsFilter(request.GET,queryset=ques_list)
    return render(request, 'paper_detail.html', {
        'filter':filter,
        'ques_list': ques_list,
        'ques_module_list': ques_module_list,
        'paper': paper_instance
    })

no_of_subquestions=0

@login_required
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

@login_required
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

@login_required
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

@login_required
def view_subques(request, id):
    ques = SubQuestions.objects.filter(id=id).get()
    return render(request, 'view_ques.html', {'ques': ques, 'id': id})

@login_required
def view_subans(request, id):
    ques = SubQuestions.objects.filter(id=id).get()
    return render(request, 'view_ans.html', {'ques': ques, 'id': id})

@login_required
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

def tex_pdf(id):
    paper_instance= created_paper.objects.get(id=id)
    ques_id_list = paper_instance.ques_id.split()
    ques_list = Questions_Main.objects.filter(pk__in=ques_id_list)
    quesm_id_list = paper_instance.ques_module_id.split()
    quesm_list = Question_Module.objects.filter(pk__in=quesm_id_list)
    comb_list=chain(quesm_list,ques_list)
    comb_list2=chain(quesm_list,ques_list)
    qm_size = len(quesm_list)
    ll = []
    
    cnt=1;
    
    for i in quesm_list:
        subques_temp = SubQuestions.objects.filter(question_module_id=i.id)
        ll.append((cnt,subques_temp))
        cnt=cnt+1
    with open('media/quiz.tex', 'w+') as fn:
        fn.write("\\documentclass[12pt]{article}\n")
        fn.write("\\usepackage[a4paper,bottom=0.6in,left=0.75in,right=0.75in,top=0.6in]{geometry}\n")
        fn.write("\\usepackage{seqsplit}\n")
        fn.write("\\usepackage{amsmath}\n")
        fn.write("\\usepackage{fancyhdr}\n")
        fn.write("\\pagestyle{fancy}\n")
        fn.write("\\lhead{Name \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ } \n")
        fn.write("\\rhead{Roll No. \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_} \n")
        fn.write("\\renewcommand{\\headrulewidth}{0.4pt} \n")
        fn.write("\\usepackage{pgf} \n")
        fn.write("\\usepackage{pgfpages} \n")
        fn.write("\\usepackage{graphicx}\n")
        fn.write("\\pgfpagesdeclarelayout{boxed}{ \\edef\\pgfpageoptionborder{3pt} } {\n")
        fn.write("\\pgfpagesphysicalpageoptions \n")
        fn.write("{ \n")
        fn.write(" logical pages=1,% \n")
        fn.write("} \n")
        fn.write("\\pgfpageslogicalpageoptions{1}{ \n")
        fn.write(" border code=\\pgfsetlinewidth{2pt}\\pgfstroke,% \n")
        fn.write("border shrink=\\pgfpageoptionborder, \n")
        fn.write("resized width=.90\\pgfphysicalwidth,\n")
        fn.write("resized height=.90\\pgfphysicalheight, \n")
        fn.write("center=\\pgfpoint{.5\\pgfphysicalwidth}{.5\\pgfphysicalheight} }} \n")
        fn.write("\\pgfpagesuselayout{boxed} \n")
        fn.write("\\begin{document}\n")
        fn.write("\\vspace*{2cm}\n")
        fn.write("\\begin{center}\n")
        fn.write("{\\Huge "+paper_instance.name+"}\\"+"\\ \n")
        fn.write("\\vspace*{1cm}\n")
        fn.write("{\\Huge Duration : "+paper_instance.duration+"}\\"+"\\ \n")
        fn.write("\\vspace*{1cm}\n")
        fn.write("{\\Huge Marks : "+str(paper_instance.marks)+"}\\"+"\\ \n")
        fn.write("\\vspace*{1cm}\n")
        fn.write("\\resizebox{1\\textwidth}{!}{% \n")
        fn.write("\\begin{tabular}{|c|c|c|}\n")
        fn.write("\\hline ")
        fn.write("Question No. & Maximum marks & Marks Obtained \\"+"\\ \n")
        fn.write("\\hline ")
        j=1
        for ques in comb_list:
            fn.write(str(j)+"&"+str(ques.marks)+"&"+" "+" \\"+"\\ \n")
            fn.write("\\hline ")
            j=j+1
        fn.write("\\end{tabular} }\n")
        fn.write("\\pagebreak \n")
        fn.write("\\end{center}\n")
        fn.write("\\begin{enumerate}\n")
        for ques in ques_list:
            if(ques.qtype==1):
                fn.write("\\item "+"{\\large "+ques.statement+"}\n")
                fn.write("\\hspace*{\\fill} {\\large ["+str(ques.marks)+" marks]}")
                fn.write("\\vspace*{"+str(1.5*ques.marks)+"cm}\n")
            elif(ques.qtype==2):
                lst=ques.statement.split('\n')
                fn.write("\\item "+"{\\large (Single Correct) \\"+"\\ "+lst[0]+"\\"+"\\ "+"\\"+"\\ "+lst[1]+"\\"+"\\ "+lst[3]+"\\"+"\\ "+lst[3]+"\\"+"\\ "+lst[4]+"} \n")
                fn.write("\\hspace*{\\fill} {\\large ["+str(ques.marks)+" marks]}")
                fn.write("\\vspace*{2cm}\n")
            elif(ques.qtype==3):
                lst=ques.statement.split('\n')
                fn.write("\\item "+"{\\large (Multiple Correct) \\"+"\\ "+lst[0]+"\\"+"\\ "+"\\"+"\\ "+lst[1]+"\\"+"\\ "+lst[3]+"\\"+"\\ "+lst[3]+"\\"+"\\ "+lst[4]+"} \n")
                fn.write("\\hspace*{\\fill} {\\large ["+str(ques.marks)+" marks]}")
                fn.write("\\vspace*{2cm}\n")
                # fn.write("\\item "+"{\\large (Multiple Correct) \\"+"\\ "+ ques.statement+"} \n")
            elif(ques.qtype==4):
                lst=ques.statement.split('\n')
                fn.write("\\item "+"{\\large "+lst[0]+"}\n")
                fn.write("\\hspace*{\\fill} {\\large ["+str(ques.marks)+" marks]} \\"+"\\ "+"\\"+"\\ \n")
                fn.write("\\resizebox{0.50\\textwidth}{!}{% \n")
                fn.write("\\begin{tabular}{|c|c|}\n")
                fn.write("\\hline ")
                for i in range(1,5):
                    fn.write(lst[i]+"&"+lst[i+4]+" \\"+"\\ \n")
                    fn.write("\\hline ")
                fn.write("\\end{tabular} }\n")
                fn.write("\\vspace*{2cm}\n")     
            
        for quesm in quesm_list:
            fn.write("\\item "+"{\\large "+quesm.statement+"}\n")
            fn.write("\\hspace*{\\fill}{\\large ["+str(quesm.marks)+" marks]}")
            subques_list = SubQuestions.objects.filter(question_module_id=quesm.id)
            fn.write("\\begin{enumerate}\n")
            for subques in subques_list:
                    fn.write("\\item "+"{\\large "+subques.statement+"}\n")
                    fn.write("\\hspace*{\\fill}{\\large ["+str(subques.marks)+" marks]}")
                    fn.write("\\vspace*{"+str(1.5*subques.marks)+"cm}\n")
            fn.write("\\end{enumerate}\n")            
        fn.write("\\end{enumerate}\n")
        fn.write("\\pagebreak")
        fn.write("{\\Huge Scratch Space}")
        fn.write("\\end{document}\n")    
    os.system("pdflatex -output-directory media media/quiz.tex")


def generate_pdf(request,id):
    tex_pdf(id)
    with open('media/quiz.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response
    pdf.closed    