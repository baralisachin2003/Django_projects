from django.shortcuts import render,redirect

# to check user is logged in or not

def unauthenticate_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function


#give access to adminpage if the request comes form admin
#give access to user dashboard if the request comes form normal user

def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function

# give access to userpage if the request comes from user.
# give access to admin dashboard if the request comes form admin

def user_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('/account/dashboard')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function



