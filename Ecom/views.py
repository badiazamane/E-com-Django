from Ecom.models import User, Product, Category, Subcategory, PurchaseHistory
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404  # n


def index(request):
    """View function for home page of site."""

    products = Product.objects.filter(is_active=True)

    paginator = Paginator(products, 4)  # Show 6 products per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "products": products,
        "username": request.user.username,
        "page_obj": page_obj,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class addAnnouncement(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(addAnnouncement, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["username"] = self.request.user.username
        return context


@login_required
def create_product(request):
    print("This message will be logged in the console.")

    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_name = request.POST.get("category")
        subcategory_name = request.POST.get("subcategory")
        user_id = request.user.id
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
            categories=category_obj,
            subcategories=subcategory_obj,
            user_id=request.user.id,
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

    return render(request, "registration/register.html", {"form": form})


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
                    "index"
                )  # Redirect to the home page or any other desired page
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})


def my_products(request):
    if request.user.is_authenticated:
        # Retrieve the products belonging to the logged-in user
        products = Product.objects.filter(user=request.user)
        paginator = Paginator(products, 4)  # Show 4 products per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "products": products,
            "username": request.user.username,
            "page_obj": page_obj,
        }

        return render(request, "my_products.html", context)
    else:
        # User is not authenticated, redirect to login page or handle the case accordingly
        return redirect("login")


def my_history(request):
    if request.user.is_authenticated:
        # Retrieve the products belonging to the logged-in user
        PurchaseHistoryProduct = PurchaseHistory.objects.filter(user=request.user)
        paginator = Paginator(PurchaseHistoryProduct, 4)  # Show 4 products per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "PurchaseHistoryProduct": PurchaseHistoryProduct,
            "username": request.user.username,
            "page_obj": page_obj,
        }

        return render(request, "my_history.html", context)
    else:
        # User is not authenticated, redirect to login page or handle the case accordingly
        return redirect("login")


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product}
    return render(request, "Ecom/product_details.html", context)


@login_required
def purchase_product(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        PurchaseHistory.objects.create(user=request.user, product=product)
        product.is_active = False
        product.save()
        # Redirect to the appropriate page after the purchase
        return redirect("index")

    return render(request, "purchase_product.html", {"product_id": product_id})


def about_us(request):
    return render(request, "about_us.html")
