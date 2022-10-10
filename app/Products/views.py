from glob import escape
import re
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from .models import Category

# Create your views here.


class Index(TemplateView):
    template_name = "products/index-4.html"


class Products(DetailView):
    model = Category
    template_name = "products/category-boxed.html"
    context_object_name = 'category'

    def get_object(self):
        return Category.objects.get(Name=self.kwargs.get("category"))

# class Products(DetailView):
#     model = Category
#     template_name = "products/category-big-products.html"
#     context_object_name = 'category'

#     def get_object(self):
#         return Category.objects.get(Name=self.kwargs.get("category"))


class Rentalpolicy(TemplateView):
    template_name = "products/rental-policy.html"


def Contact(request):
    if request.method == "POST":
        message_name = request.POST['nameContact']
        message_surname = request.POST['surnameContact']
        message_email = request.POST['emailContact']
        message = request.POST['messageContact']

        print(message_email)
        send_mail(
            f"{message_name} {message_surname}  {message_email}",
            message,
            message_email,
            ["info@enchantedrentals.org"],
            fail_silently=False,
        )
        message = "Succesfully sent message, We will get back to you shortly"

        return render(request, "products/contact.html", context={"message": message})

    return render(request, "products/contact.html")
