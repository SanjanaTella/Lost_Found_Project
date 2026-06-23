from django.shortcuts import render, redirect
from .forms import SignUpForm, FoundItemForm, LostItemForm
from .models import FoundItem, LostItem
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request): 
    if request.method == 'POST': 
        form = SignUpForm(request.POST)  
        if form.is_valid():            
            user = form.save()             
            login(request, user)  
            return redirect('home')  # Use URL name, not template
        else: 
            messages.error(request, "Signup failed. Please fix the errors below.")
    else: 
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
        except Exception as e:
            messages.error(request, f"Error during login: {e}")

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


@login_required
def report_found(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoundItemForm()

    return render(request, 'found_item.html', {'form': form})
    return render(request, 'match_item.html', {'form': form})


def item_submitted(request):
    return render(request, 'item_submitted.html')


@login_required
def report_lost(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST)
        if form.is_valid():
            lost_item = form.save(commit=False)
            lost_item.user = request.user
            lost_item.save()

            messages.success(request, "Item reported as lost successfully!")

            # Matching logic
            matches = FoundItem.objects.filter(item_name__icontains=lost_item.item_name)
            if matches.exists():
                matched = matches.first()
                send_mail(
                    'Match Found for Your Lost Item',
                    f"Your item '{matched.item_name}' might have been found at {matched.location}.",
                    'admin@lostfound.com',
                    [request.user.email],
                    fail_silently=False,
                )
                return render(request, 'match_item.html', {'match': matched})
            else:
                return render(request, 'match_item.html', {'match': None})
    else:
        form = LostItemForm()
    return render(request, 'lost_item.html', {'form': form})

def match_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item submitted successfully!')
            return redirect('match_item')  # Redirect to clear form and show message
    else:
        form = FoundItemForm()
    return render(request, 'match_item.html', {'form': form})