from Ecom.models import User, Product
from django.shortcuts import render
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Users = User.objects.all().count()

    context = {
        "num_Users": num_Users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class addAnnouncement(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(addAnnouncement, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["some_data"] = "This is just some data"
        return context
