from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Maison, UserProfile


def index(request):
    return render(request,'index.html')

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username "{username}" is already used 📢😉.')
                return redirect('sign-up')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already used 📢😉.')
                return redirect('sign-up')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'You have successfully registered. You can now login ❤️.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match ⚠️')
            return render(request, 'register.html')
    else :
        return render(request,'register.html')
def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credentiels not valid ⚠️")
            return redirect('login')
    else :
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def dashboard(request):
    current_user = request.user 
    if request.method == 'POST':
        house_key  = request.POST['house_key']
        house_address = request.POST['house_address']
        house_name = request.POST['house_name']
        try:
            house = Maison.objects.get(key=house_key,address=house_address,name=house_name)
            messages.success(request,f"Successfully authenticated to {house.name}")
            user_profile, created = UserProfile.objects.get_or_create(user=current_user)
            user_profile.maison.add(house)
            list_parm = []
            with open('static\js\data.json','r') as f :
                list_parm = f.readlines()
            context = {
                'house_name':house_name,
                'list_parm' : list_parm ,
            }

            return render(request,'dashboard.html',context=context)
        except Maison.DoesNotExist :
            messages.error(request,'Invalid house key or address')
    return render(request,'monitoring.html')

def dashborad_views(request):
    return render(request,'weather.html')