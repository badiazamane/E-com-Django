from Ecom.models import User, Product, Category, Subcategory
from django.shortcuts import render, redirect
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Get all products
    products = Product.objects.all()

    context = {
        "products": products,
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
        category_name = request.POST.get("category")
        subcategory_name = request.POST.get("subcategory")
        image = request.FILES.get("image")
        print(image)
        # # Get or create category object
        category_obj, _ = Category.objects.get_or_create(name=category_name)

        # # Get or create subcategory object
        subcategory_obj, _ = Subcategory.objects.get_or_create(name=subcategory_name)

        # Create new product object
        product = Product(
            name=name,
            description=description,
            price=price,
            # # ...
            categories=category_obj,
            subcategories=subcategory_obj,
            image=image,
        )

        # Save the product to the database
        product.save()

        # Redirect to a success page or perform any other desired action
        return redirect("success")

    return render(request, "product_list.html")


def success_view(request):
    return render(request, "success.html")
