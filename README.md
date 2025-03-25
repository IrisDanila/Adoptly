# Adoptly

Adoptly is a Django-based web application designed to connect people with animals in need of adoption. The platform allows users to browse available animals, submit adoption requests, and even detect dog breeds using an image classification feature.

---

## Features

- **Animal Listing**: View a list of animals available for adoption, complete with details like name, species, breed, age, and an image.
- **Adoption Requests**: Submit adoption requests for specific animals with a user-friendly form.
- **Dog Breed Detection**: Upload an image of a dog to detect its breed using a machine learning model.
- **Responsive Design**: The app is styled with Bootstrap for a clean and responsive user interface.

---

## Technologies Used

- **Backend**: Django 5.1.6
- **Frontend**: Bootstrap 4.5.2, Crispy Forms
- **Database**: SQLite (default Django database)
- **Machine Learning**: Hugging Face Transformers for dog breed detection
- **Other Libraries**:
  - `django-rest-framework` for API support
  - `django-extensions` for development utilities
  - `pillow` for image handling

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd adoptly
   
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Usage

### Home Page
The home page introduces the platform and provides links to browse available animals or start the adoption process.

### Animal Listing
- Navigate to `/animals_list/` to view all available animals.
- Each animal card includes details and a button to submit an adoption request.

### Adoption Request
- Click the "Adopt" button on an animal card to access the adoption request form.
- Fill out the form and submit your request.

### Dog Breed Detection
- Navigate to `/breed_detection/` to upload an image of a dog and detect its breed.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.