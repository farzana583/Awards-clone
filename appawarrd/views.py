from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import  CreateUserForm,NewPostForm, UserUpdateForm, ProfileUpdateForm,SignUpForm
from .models import Image,Ratings
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='accounts/login/')
@csrf_exempt
def home(request):
    all_posts = Image.all_images()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                 request.FILES, 
                                 instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
        'u_form': u_form,
        'p_form': p_form,
        'all_posts': all_posts
    }
    return render(request, 'index.html', context)

    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
    	if request.user.is_authenticated:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:                                                               
                messages.info(request,'Username OR password is incorrect')	
            context = {}
            return render(request,'registration/login.html',context)
        
# def rate(request,id):
#     if request.method =='POST':
#         rates = Ratings.objects.filter(id = id)
#         for rate in rates:
#             if rate.user == request.user:
#                 messages.info(request,'You cannot rate a project twice')
#                 return redirect('singleproject',id)
#         design = request.POST.get('design')
#         usability = request.POST.get('usability')
#         content = request.POST.get('content')
#         if design and usability and content:
#             project = Image.objects.get(id = id)
#             rate = Ratings(design = design,usability = usability,content = content,project_id = project,user = request.user)
#             rate.save()
#             return redirect('singleproject',id)
#         else:
#             messages.info(request,'Input all fields')
#             return redirect('singleproject',id)
#     else:
#         messages.info(request,'Input all fields')
#         return redirect('singleproject',id)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='accounts/login/')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

@login_required(login_url='accounts/login/')
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.image_poster = request.user
            image.save()
        return redirect('/')

    else:
        form = NewPostForm()
    return render(request, 'post_image.html', {'form': form})

def registerPage(request):

    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['username']
            email = form.cleaned_data['email']
            send=welcome_email(name,email)
            HttpResponseRedirect('home')
    else:
        form = SignUpForm()
    return render(request,'registration/registration_form.html',{'form':form})

@login_required(login_url='accounts/login/')
def rate(request,id):
    if request.method =='POST':
        rates = Ratings.objects.filter(id = id)
        for rate in rates:
            if rate.user == request.user:
                messages.info(request,'You cannot rate a project twice')
                return redirect('singleproject',id)
        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')
        if design and usability and content:
            project = Image.objects.get(id = id)
            rate = Ratings(design = design,usability = usability,content = content,project_id = project,user = request.user)
            rate.save()
            return redirect('singleproject',id)
        else:
            messages.info(request,'Input all fields')
            return redirect('singleproject',id)
    else:
        messages.info(request,'Input all fields')
        return redirect('singleproject',id)

def single_project(request,id):  
    project = Image.objects.get(id = id)
    rates = Ratings.objects.filter(project_id = id)
    designrate = []
    usabilityrate = []
    contentrate = []
    if rates:
        for rate in rates:
            designrate.append(rate.design)
            usabilityrate.append(rate.usability)
            contentrate.append(rate.content)
        total = len(designrate)*10
        design = round(sum(designrate)/total*100,1)
        usability = round(sum(usabilityrate)/total*100,1)
        content = round(sum(contentrate)/total*100,1)
        return render(request,'single_project.html',{'project':project,'design':design,'usability':usability,'content':usability})
    else:
        design = 0
        usability = 0
        content = 0       
        return render(request,'single_project.html',{'project':project,'design':design,'usability':usability,'content':usability})
    # if request.method == 'POST':
    #     form = CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Your account has been created successfully!')
    #         return redirect('login')
    # else:
    #     form = CreateUserForm()
    # return render(request, 'registration/registration_form.html', {'form': form})