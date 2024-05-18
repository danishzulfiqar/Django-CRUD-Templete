from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import CreateRecordForm, UpdateRecordForm


# home page
def index(request):
    return render(request, "webapp/index.html")


# Register user
def register(request):

    # if user is authenticated, redirect to dashboard
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = CustomUserCreationForm()
    if request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            # messages.success(request, "Account created successfully!")

            return redirect("login")

    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)


# Login user
def login(request):

    # if user is authenticated, redirect to dashboard
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/login.html', context=context)


# Dashboard
@login_required(login_url='login')
def dashboard(request):

    # Sending recorrds to the template
    records = Record.objects.all()

    context = {'records': records}

    return render(request, 'webapp/dashboard.html', context=context)


# CRUD
# Create record
@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)

# Create api request sample for postman
# {
#     "name": "John Doe",
#     "email": "testing@gmail.com",
#     "phone": "1234567890",
#     "address": "123, New York",
#}  

# Update record
@login_required(login_url='login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/update-record.html', context=context)


# view record
@login_required(login_url='login')
def view_record(request, pk):

    record = Record.objects.get(id=pk)

    context = {'record': record}

    return render(request, 'webapp/view-record.html', context=context)


# Delete record
@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    return redirect("dashboard")



# Logout user
def logout(request):

    auth.logout(request)

    return redirect("login")
