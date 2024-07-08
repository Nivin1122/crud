from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .models import Coaches,Players
from .models import Booking
from .import forms 
from .forms import SignupForm,LoginForm


from .forms import BookingForm
from .forms import PlayersForm
from .forms import CoachForm

# Create your views here.
def index(request):
    return render(request,"index.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('players')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form' : form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('players')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form' : form})


def players(request):
    all_players = Players.objects.all()

    context = {
        'all_players' : all_players
    }
    return render(request,"players.html",context)


def delete_players(request,id):
    obj = get_object_or_404(Players,pk=id)
    obj.delete()
    return redirect('players')



def coaches(request):

    all_coaches = Coaches.objects.all()

    return render(request,"coaches.html",{'all_coaches':all_coaches})


def delete_coaches(request,id):
    obj = get_object_or_404(Coaches,pk=id)
    obj.delete()
    return redirect('coaches')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"confirmation.html")
    form = BookingForm()
    context = {
        'form' : form
    }
    return render(request,"booking.html",context)





def confirmation(request):
    return render(request,"confirmation.html")


def ticket_list(request):
    all_tickets = Booking.objects.all()

    context = {
        'all_tickets' : all_tickets
    }
    return render(request,"ticket_list.html",context)


def edit_tickets(request,id):
    ticket = get_object_or_404(Booking,id=id)
    if request.method == "GET":
        context = {'form' : BookingForm(instance=ticket),'id':id}
        return render(request,"edit_tickets.html",context)
    else:
        if request.method == "POST":
            form = BookingForm(request.POST,instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('ticket_list')
            else:
                messages.error(request,"error")
                return render(request,"edit_tickets.html",{'form' : form})
            
def delete_tickets(request,id):
    obj = get_object_or_404(Booking,pk=id)
    obj.delete()
    return redirect('ticket_list')
            


def add_players(request):
    if request.method == "POST":
        form = PlayersForm(request.POST,request.FILES)

        print(form)
        if form.is_valid():
            form.save()
            return redirect('players')
        else:
            print("else valid")
    else:
        form = PlayersForm()
    
    return render(request,"add_players.html",{'form' : form})


def edit_players(request,id):
    player = get_object_or_404(Players,id=id)
    if request.method == "GET":
        context = {'form':PlayersForm(instance=player),'id':id}
        return render(request,'edit_players.html',context)

    elif request.method == "POST":
        form = PlayersForm(request.POST,request.FILES,instance=player)
        if form.is_valid():
            form.save()
            return redirect('players')
        else:
            messages.error(request,'error')
            return render(request,'edit_players.html',{'form':form})


def add_tickets(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = BookingForm()
    return render(request,"add_tickets.html",{'form' : form})


def add_coaches(request):
    # form = CoachForm()
    if request.method == "POST":
        form = CoachForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coaches')
    else:
        form = CoachForm()
    context = {
        'form' : form
    }
    return render(request,"add_coaches.html",context)


def edit_coaches(request,id):
    coach = Coaches.objects.get(id=id)
    if request.method == "POST":
        form = CoachForm(request.POST,request.FILES,instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coaches')
    else:
        form = CoachForm(instance=coach)
    context = {
        'form' : form
    }
    return render(request,"edit_coaches.html",context)


def contact_us(request):
    return render(request,"contact_us.html")