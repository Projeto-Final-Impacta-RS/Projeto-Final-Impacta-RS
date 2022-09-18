from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse

from .forms import *
from .models import *

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questoes=Questao.objects.all()
        pontuacao=0
        erros=0
        acertos=0
        total=0
        for questao in questoes:
            total+=1
            print(request.POST.get(questao.descricao))
            print(questao.resposta)
            print()
            if 'alternativa' + questao.resposta == request.POST.get(questao.descricao):
                pontuacao+=10
                acertos+=1
            else:
                erros+=1
        percentual = pontuacao/(total*10) *100
        context = {
            'pontuacao':pontuacao,
            'tempo': request.POST.get('cronometro'),
            'acertos':acertos,
            'erros':erros,
            'percentual':percentual,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questoes=Questao.objects.all()
        context = {
            'questoes':questoes
        }
        return render(request,'home.html',context)

def addQuestion(request):  
    if request.user.is_staff:  
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    else: 
        return redirect('home')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')


