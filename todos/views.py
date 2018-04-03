from django.shortcuts import render
from django.views.generic import DetailView, ListView


from todos.models import List


# Create your views here.
class ListArchiveView(ListView):
    model = List


class ListDetailView(DetailView):
    model = List
