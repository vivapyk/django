from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from accounts.forms import SignupForm


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })

