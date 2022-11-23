from django.shortcuts import render
from django.contrib import messages

# Create your views here.
# Create your views here.
def register(request):
    register = register.objects.all()

    context_dict = {"register": register}

    return render(
        request = request,
        context = context_dict,
        template_name="register/register.html",
    )

