from django.shortcuts import render,redirect
from.forms import UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def login(request):
    form=UserLoginForm()
    if request.method=='POST' and 'login' in request.POST:
        form=UserLoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                print("user in if condition")
                login(request,user)
                return redirect('index')
        
            else:
                print("user is not authenticated")
                return redirect('login')
            # return redirect('index')
        else:
            print("back to login")
            messages.warning(request,'Enable to Login')
            return redirect('login_view')
    else:
        form=UserLoginForm()
        messages.warning(request,'Login Unsuccessful ,Please Try Again ')
    context={
        'form':UserLoginForm
    }
    return render(request,'Dashboard/index.html',{'form': form })