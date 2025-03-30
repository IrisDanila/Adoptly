from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from .models import Animal, AdoptionRequest
from .serializers import AnimalSerializer
from .forms import AdoptionRequestForm, BreedDetectionForm
from .utils.breed_detection import BreedDetector
from django.contrib.auth import login, logout, authenticate
from .forms import UserSignupForm, UserLoginForm


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

def animals_list(request):
    search_query = request.GET.get('q', '')
    animals = Animal.objects.filter(is_available=True)
    if search_query:
        animals = animals.filter(name__icontains=search_query)
    return render(request, 'adoptions/animals_list.html', {'animals': animals, 'search_query': search_query})

def home(request):
    return render(request, 'adoptions/home.html')

def adoption_request(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.animal = animal
            adoption_request.save()
            return redirect('success_page')  # Redirect to a success page after submission
    else:
        form = AdoptionRequestForm()

    return render(request, 'adoptions/adoption_request.html', {'animal': animal, 'form': form})

def success_page(request):
    return render(request, 'adoptions/success.html')



from django.http import JsonResponse

def breed_detection(request):
    if request.method == 'POST':
        form = BreedDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            detector = BreedDetector()
            result = detector.detect_breed(image)  # Call the detect_breed method
            # Return JSON response for AJAX requests
            return JsonResponse({'breed': result})
        else:
            # Return errors as JSON if form is invalid
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        form = BreedDetectionForm()

    # Render the HTML template for non-AJAX requests
    return render(request, 'adoptions/breed_detection.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'adoptions/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'adoptions/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')





from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_authenticated and u.is_admin)
def requests_view(request):
    adoption_requests = AdoptionRequest.objects.all()
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        adoption_request = get_object_or_404(AdoptionRequest, id=request_id)

        if action == 'accept':
            adoption_request.animal.delete()  # Delete the animal
            adoption_request.delete()  # Delete the request
        elif action == 'decline':
            adoption_request.delete()  # Only delete the request

        return redirect('requests')

    return render(request, 'adoptions/requests.html', {'adoption_requests': adoption_requests})

from .forms import AnimalForm

@user_passes_test(lambda u: u.is_authenticated and u.is_admin)
def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animals_list')
    else:
        form = AnimalForm()
    return render(request, 'adoptions/add_animal.html', {'form': form})