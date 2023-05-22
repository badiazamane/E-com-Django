from Ecom.models import User, Product, Category, Subcategory
from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Users = User.objects.all().count()
    num_visits = request.session.get("num_visits", 0)

    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        num_visits = request.session.get("num_visits", 0)
        request.session["num_visits"] = num_visits + 1
    else:
        num_visits = -1
    context = {
        "num_Users": num_Users,
        "num_visits": num_visits,
    }

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
        user_id = request.POST.get("user")
        image = request.FILES.get("image")
        print(user_id)

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


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    "home"
                )  # Redirect to the home page or any other desired page
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
