from django.shortcuts import render, redirect
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()
    
    return render(request, 'contact.html', {'form': form})