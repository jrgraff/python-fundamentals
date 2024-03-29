from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'layout/home.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return redirect('property:list')
