from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from federations.models import Federation


def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add(Q(official_website__contains=search_param), Q.OR)
        federations = Federation.objects.filter(query)
        context_dict.update(
            {
                "federations": federations,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )