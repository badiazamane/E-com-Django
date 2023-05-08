from Ecom.models import User, Product
from django.shortcuts import render, redirect
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


def create_product(request):
    print("This message will be logged in the console.")
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = request.POST.get("category")
        subcategory = request.POST.get("subcategory")

        # Create new product object
        product = Product(
            name=name,
            description=description,
            Price=price,
            # Assign the appropriate foreign keys
            # For example, if you have related models User, Category, and subCategory:
            #! Seller_ID=request.user,  # Assuming the user is authenticated
            Categories_ID=category.objects.get(name=category),
            subCategories_ID=subcategory.objects.get(name=subcategory),
        )

        # Save the product to the database
        product.save()

        # Redirect to a success page or perform any other desired action

        return redirect("success")

    return render(request, "product_list.html")
