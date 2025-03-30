from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import migrations
from django.contrib.auth import get_user_model

class Animal(models.Model):
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Rabbit', 'Rabbit'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='animal_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AdoptionRequest(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    about_you = models.TextField(blank=True)
    reason_for_adoption = models.TextField(blank=True)  # New field
    experience_with_pets = models.TextField(blank=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Adoption Request for {self.animal.name} by {self.name}"
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_regular_user = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    


# creating the admin 

def create_admin_user(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(email="admin@adoptly.com").exists():
        User.objects.create_superuser(
            email="admin@adoptly.com",
            username="admin",
            password="adminpassword",
            is_admin=True,
            is_regular_user=False,
        )



class Migration(migrations.Migration):
    dependencies = [
        ('adoptions', '0001_initial'),  # Replace with the actual name of your initial migration file
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]


