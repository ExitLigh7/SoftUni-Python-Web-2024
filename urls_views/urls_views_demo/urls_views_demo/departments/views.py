from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from urls_views_demo.departments.models import Department


def index(request):
    url = reverse('redirect-view')
    url_lazy = reverse_lazy('redirect-view')
    return HttpResponse(f"<h1>{url_lazy}</h1>")

def view_with_name(request, variable):
    # return HttpResponse(f"<h1>Variable is: {variable}</h1>")
    return render('departments/name_template.html', {'variable': variable})

def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int PK is: {pk}</h1>")

def view_with_slug(request, pk, slug):
    # Option 1 for 404

    # department = Department.objects.filter(pk=pk,slug=slug)
    # if not department:
    #     raise Http404

    # Option 2

    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")

def show_archive(request, archive_year):
    return HttpResponse(f"<h1>Archive year: {archive_year}</h1>")

def redirect_to_softuni(request):
    return redirect('https://softuni.bg')

def redirect_to_view(request):
    return redirect('home')