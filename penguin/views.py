from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from users.models import Library
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.


product = Product.objects.all()
prodcat = Product.objects.values("category")
cats = {x["category"] for x in prodcat}
plst = [Product.objects.filter(category=cat) for cat in cats]
params = {"plst": plst}


def index(request):

    return render(request, "penguin/index.html", params)


def searchMatch(query, item):

    query = query.lower()

    if (
        query in item.product_name.lower()
        or query in item.category.lower()
        or query in item.desc.lower()
        or query in item.subcategory.lower()
    ):

        return True

    else:

        return False


def search(request):
    query = request.GET.get("search")
    items = []
    if query != "":
        for i in product:
            if searchMatch(query, i):
                items.append(i)
    params["items"] = items
    return render(request, "penguin/search.html", params)


class ViewAll(ListView):
    model = User
    template_name = "penguin/viewall.html"
    context_object_name = "items"
    paginate_by = 9

    def get_queryset(self):
        uitems = Product.objects.filter(category=self.kwargs["cat"])
        return uitems

    def get_context_data(self, **kwargs):
        context = super(ViewAll, self).get_context_data(**kwargs)
        context["plst"] = plst
        return context


def view(request, pid):
    if request.user.is_authenticated:
        u = request.user
        lib = u.library.user_items.all()
        params["lib"] = lib
    get_prod = Product.objects.filter(id=pid)
    params["get_prod"] = get_prod
    return render(request, "penguin/view.html", params)


@login_required
def checkout(request, pid):
    u = request.user
    p = Product.objects.get(id=pid)
    u.library.user_items.add(p)
    messages.success(
        request, "Succesfully added to library (After Abstract Payment -_- ) !!"
    )
    return redirect("home")
