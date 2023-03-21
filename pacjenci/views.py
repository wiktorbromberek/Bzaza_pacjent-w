from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import *
from .filters import PacjentFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only




@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            passw = form.cleaned_data.get('password')
            group = Group.objects.get(name='pacjent')
            user.groups.add(group)
            messages.success(request,'Account created for '+ username)
            Pacjent.objects.create(user=user)
            return redirect('login')
        else:
             messages.info(request,'Wprowadzono niepoprawne dane ')

    context={'form':form}
    return render(request, 'pacjenci/register.html',context)

@unauthenticated_user
def loginPage(request):
    
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is INCORRECT')



    context={}
    return render(request, 'pacjenci/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    wizyts = Wizyta.objects.all()
    pacjents = Pacjent.objects.all()
    total_pacjents=pacjents.count()
    total_wizyts = wizyts.count()



    context = {'wizyts':wizyts,'pacjents':pacjents, 'total_pacjents':total_pacjents,
    'total_wizyts':total_wizyts}

    return render(request,'pacjenci/dashboard.html',context)

# @login_required(login_url='login')    
# @allowed_users(allowed_roles=['admin'])
def lekarzs(request):
    lekarzes = Lekarz.objects.all()
    return render(request,'pacjenci/lekarzs.html',{'lekarzes':lekarzes})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pacjent(request,pk):
    pacjent = Pacjent.objects.get(id=pk)
    wizyts = pacjent.wizyta_set.all()
    wizyts_count = wizyts.count()
     
    myFilter = PacjentFilter(request.GET, queryset=wizyts)
    wizyts = myFilter.qs

    context = {'pacjent':pacjent,'wizyts':wizyts,'wizyts_count':wizyts_count,'myFilter':myFilter}
    return render(request,'pacjenci/pacjent.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['pacjent'])
def userPage(request):
    wizyts = request.user.pacjent.wizyta_set.all()
    total_wizyts=wizyts.count()

    # delivered = wizyts.filter(status='Delivered').count()
    # pending = wizyts.filter(status='Pending').count()
# 'delivered':delivered,'pending':pending
    context={'wizyts':wizyts,'total_wizyts':total_wizyts,}
    return render(request, 'pacjenci/user.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['pacjent'])
def ustawieniaKonta(request):
    pacjent = request.user.pacjent
    form = PacjentForm(instance=pacjent)
    if request.method == 'POST':
         form = PacjentForm(request.POST, instance=pacjent)
         if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'pacjenci/user_settings.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createWizyta(request,pk):
    WizytaFormSet = inlineformset_factory(Pacjent,Wizyta, fields=('date','lekarz','pacjent','oddział','content'), extra=1)
    pacjent = Pacjent.objects.get(id=pk)
    formset = WizytaFormSet(queryset=Wizyta.objects.none(), instance=pacjent)
    if request.method == 'POST':
        formset = WizytaFormSet(request.POST,instance=pacjent)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}

    return render(request, 'pacjenci/wizyta_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateWizyta(request,pk):

    wizyta = Wizyta.objects.get(id=pk)
    form=WizytaForm(instance=wizyta)

    if request.method == 'POST':
        form=WizytaForm(request.POST, instance=wizyta)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, 'pacjenci/update_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteWizyta(request,pk):
    wizyta = Wizyta.objects.get(id=pk)
    if request.method == 'POST':
        wizyta.delete()
        return redirect('/')
    context = {'item':wizyta}
    return render(request,'pacjenci/delete.html',context)