from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.db.models import Sum
from .models import Link
from .forms import UserRegistrationForm, LinkCreateForm

def home(request):
    return render(request, 'shortener/home.html')

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('shortener:dashboard')
    template_name = 'shortener/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Account created successfully!')
        return response

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('shortener:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'shortener/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('shortener:home')

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = LinkCreateForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            messages.success(request, 'Link shortened successfully!')
            return redirect('shortener:dashboard')
    else:
        form = LinkCreateForm()

    links = Link.objects.filter(user=request.user).order_by('-created_at')
    total_clicks = links.aggregate(total=Sum('click_count'))['total'] or 0
    avg_clicks = round(total_clicks / links.count()) if links.exists() else 0

    return render(request, 'shortener/dashboard.html', {
        'form': form,
        'links': links,
        'total_clicks': total_clicks,
        'avg_clicks': avg_clicks
    })

@login_required
def profile(request):
    total_clicks = Link.objects.filter(user=request.user).aggregate(total=Sum('click_count'))['total'] or 0
    return render(request, 'shortener/profile.html', {
        'total_clicks': total_clicks
    })

def redirect_to_url(request, short_code):
    link = get_object_or_404(Link, short_code=short_code)
    link.click_count += 1
    link.save()
    return redirect(link.original_url)
