from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from penguin.models import Product
from django.views.generic import ListView
from .models import Library
from django.contrib.auth.models import User


product = Product.objects.all()
prodcat = Product.objects.values("category")
cats = {x["category"] for x in prodcat}
plst = [Product.objects.filter(category=cat) for cat in cats]

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username} !!")
            return redirect("login")
    else:
        form = UserRegisterForm
    return render(request, "users/register.html", {"form": form})


class UserLibrary(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/library.html"
    context_object_name = "items"
    paginate_by = 9

    def get_queryset(self):
        u = self.request.user
        uitems = u.library.user_items.all()
        return uitems

    def get_context_data(self, **kwargs):
        context = super(UserLibrary, self).get_context_data(**kwargs)
        context["plst"] = plst
        return context
