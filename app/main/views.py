from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
from .models import User,Mood

def register(request):
    if('user_id' in request.session):
        return HttpResponse('вы уже зарегестрированы или хотите выйти с аккаунта,но можете потерят этот аккаунт безвозвратно. ')
    elif(request.method == "GET"):
        return render(request,'register.html')
    else:
        username = request.POST.get('username','')
        if(username == ''):
            return HttpResponse('некорректное имя')
        user = User.objects.create(username=username)
        request.session['user_id'] = user.id
        return redirect('/')

def main_menu(request):
    if('user_id' in request.session):
        user = User.objects.get(id=request.session['user_id'])
        moods = user.mood.all()
        return render(request,'menu.html',{'user':user,'mood':moods})
    else:
        redirect('/register/')

def createMood(request):
    if('user_id' in request.session):
        if(request.method == 'GET'):
            return render(request,'create-mood.html')
        else:
            user_mood = request.POST.get('mood','')
            comment = request.POST['coment']
            if(user_mood == ''):
                print(user_mood)
                return HttpResponse('некорректные данные')
            user = User.objects.get(id=request.session['user_id'])
            Mood.objects.create(users_mood=user_mood,comment=comment,user=user)
            return redirect('/')
    else:
        return redirect('/register/')
            
            
def delAccount(request):
    if('user_id' in request.session):
        user_id = request.session['user_id']
        if(User.objects.filter(id=user_id).exists()):
            User.objects.get(id=user_id).delete()
        del request.session['user_id']
        
        return redirect('/register/')