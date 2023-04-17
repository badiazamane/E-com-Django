from catalog.models import Users
from django.shortcuts import render


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Users = Users.objects.all().count()
    
    context = {
        'num_books': num_Users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
