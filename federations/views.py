from django.shortcuts import render
from django.contrib import messages
from federations.models import Federation
from federations.forms import FederationForm


# Create your views here.
def federations(request):
    federations = Federation.objects.all()

    context_dict = {"federations": federations}

    return render(
        request = request,
        context = context_dict,
        template_name="federations/federations_list.html",
    )

def create_federation(request):
    if request.method == "POST":
        federation_form = FederationForm(request.POST)
        if federation_form.is_valid():
            data = federation_form.cleaned_data
            actual_objects = Federation.objects.filter(
                name=data["name"], initials=data["initials"], official_website=data["official_website"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La federación {data['name']} - {data['initials']} ya existe",
                )
            else:
                federation = Federation(name=data["name"], initials=data["initials"], official_website=data["official_website"])
                federation.save()
                messages.success(
                    request,
                    f"Federación {data['name']} - {data['initials']} incluida exitosamente!",
                )

            federations = Federation.objects.all()

            context_dict = {"federations": federations}

            return render(
                request=request,
                context=context_dict,
                template_name="federations/federations_list.html",
            )

    federation_form = FederationForm(request.POST)
    context_dict = {"form": federation_form}
    return render(
        request=request,
        context=context_dict,
        template_name="federations/federations_form.html",
    )
