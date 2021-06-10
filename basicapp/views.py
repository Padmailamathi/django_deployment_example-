from django.shortcuts import render
from basicapp.forms import UserForm,UserProfileInfoForm
# Create your views here.

def index(request):

    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def register(request):

    registered = False
    user_form = UserForm()
    profile_form = UserProfileInfoForm()

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid() :
            user = user_form.save()
            # user.set_password(user.password)
            # user.save(commit=True)
            # profile_form.save()

    else :
        print("False")
    #
    #     if user_form.is_valid():
    #         user = user_form.save()


    # registered = True

    return render(request, 'register.html',{'user_form' : user_form , 'profile_form':profile_form, 'registered' : registered})
