from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .form import VideoModelForm, RevieModelForm
from .models import Video, Review
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms


# Create your views here.
def crud_new(request):
    form = VideoModelForm()
    return render(request, 'video/crud_new.html', {
        'form': form
    })

@require_POST
def crud_create(request):
    obj = Video()
    form = VideoModelForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 
        'Successful upload')
        return redirect('crud_new')
    else:
        return render(request, 'video/crud_new.html', {
            'form' : form
        })

def rel(request, id):
    return render(request, 'video/rel.html', {
        'video': Video.objects.get(pk=id) 
    })

@login_required
def listview(request):
    video_list = Video.objects.all() 
    return render(request, 'video/list.html', {
        'video_list' : video_list, 
        })

def showvideo(request):
    lastvideo= Video.objects.last()
    videofile= lastvideo.videofile

    form= VideoModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context= {'videofile': videofile,
              'form': form
              }
      
    return render(request, 'video/videoshow.html', context)
@login_required
def review_input(request, id):
    obj = get_object_or_404(Video, pk=id)
    rev_all = Review.objects.filter(video_id=id).all()
    review_all_user = [r.name for r in rev_all]
    print(review_all_user)
    #instance = User.objects.filter(username=request.user).first()
    form = RevieModelForm(instance=obj)
    return render(request, 'video/rev_input.html', {
        'form' : form, 
        'v' : obj, 
        'review_all_user': review_all_user
    })

@login_required
def review_edit(request, id):
    obj = get_object_or_404(Video, pk=id)
    form = RevieModelForm(instance=obj)
    return render(request, 'video/rev_edit.html', {
        'form' : form, 
        'v' : obj,
    })

@require_POST
def review_update(request, id):
    obj = Video.objects.get(pk=id)
    user_name = request.user.username
    obj_rev = obj.review_set.all()
    rev_user = obj_rev.get(name=user_name)
    form = RevieModelForm(request.POST, instance=rev_user)
    if form.is_valid():
        form_edit = form.save(commit=False)
        form_edit.name = user_name
        form_edit.save()
        print('save OK')
        return redirect('video:rev_list', id=id)
    else:
        return render(request, 'video/rev_edit.html', {
            'form' : form, 
            'v' : obj, 
        })

@login_required    
def review_delete(request, id):
    obj = Video.objects.get(pk=id)
    user_name = request.user.username
    obj_rev = obj.review_set.all()
    rev_user = obj_rev.get(name=user_name)
    rev_user.delete()
    return redirect('video:rev_list', id=id)

@login_required
def rev_new(request):
    form = RevieModelForm()
    return render(request, 'video/rev_input.html', {
        'form' : form
    })

@require_POST
def review_process(request, id):
    #obj = get_object_or_404(Video, pk=id)
    form = RevieModelForm(request.POST)
    user_name = request.user.username
    #name_id = request.user.id
    print(user_name)
    print('OKOK!')
    print(form.is_valid())
    if form.is_valid():
        new_rev = form.save(commit=False)
        new_rev.video = Video.objects.get(pk=id)
        new_rev.name = user_name
        #new_rev.name = User.objects.get(username=user_name)
        new_rev.save()
        print('save OK')
        #obj = Video.objects.all()
        #return render(request, 'video/rev_list.html', {'obj' : obj})
        return redirect('video:rev_list', id=id)
    else:
        return render(request, 'video/rev_input.html', {
            'form' : form
        })

@login_required
def rev_list(request, id):
    obj = Video.objects.all()
    id_all = [v.id for v in obj]
    return render(request, 'video/rev_list.html', {
        'obj' : obj, 
        'next_id' : id+1, 
        'id_all' : id_all
        })

def rev_list2(request):
    obj = Video.objects.all()
    return render(request, 'video/rev_list.html', {
        'obj' : obj
        })

def signupview(request):
    #print(request.POST.get('username_data'))
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'user/signup.html', {'error':'This user is already registerd.'})
    else:
        print(User.objects.all())
    return redirect('video:login')
    #return render(request, 'user/signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, 
        password=password_data)

        if user is not None:
            login(request, user)
            return redirect('video:list')
        else:
            return redirect('video:login')
    
    return render(request, 'user/login.html')

def logoutview(request):
    logout(request)
    return redirect('video:login')
