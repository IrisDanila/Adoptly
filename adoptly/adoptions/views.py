from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from .models import Animal, AdoptionRequest
from .serializers import AnimalSerializer
from .forms import AdoptionRequestForm, BreedDetectionForm
from .utils.breed_detection import BreedDetector


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




from django.shortcuts import render
from .forms import BreedDetectionForm
from .utils.breed_detection import BreedDetector

def breed_detection(request):
    breed = None  # Initialize the breed variable
    if request.method == 'POST':
        form = BreedDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            detector = BreedDetector()
            result = detector.detect_breed(image)  # Call the detect_breed method
            breed = result  # Assign the result to the breed variable
    else:
        form = BreedDetectionForm()

    return render(request, 'adoptions/breed_detection.html', {'form': form, 'breed': breed})