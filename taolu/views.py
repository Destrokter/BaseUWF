from urllib import request
from django.shortcuts import render, redirect
from .models import Taolu
from .forms import TaoluForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def taolu(request):
    taolu= Taolu.objects.order_by('name')
    paginator = Paginator(taolu, 3)
    page_number = request.GET.get('page')
    taolu = paginator.get_page(page_number)
    return render(request, 'taolu/taolu.html', {'taolu': taolu})
    #taolu = Taolu.objects.order_by('name')
    #return render(request, 'taolu/taolu.html', {'taolu':taolu})


class TaoluDetailView(LoginRequiredMixin, DetailView):
    model = Taolu
    template_name ='taolu/details_view.html'
    context_object_name = 'taolu'


class TaoluUpdateView(LoginRequiredMixin, UpdateView):
    model = Taolu
    template_name = 'taolu/create.html'

    form_class = TaoluForm


class TaoluDeleteView(LoginRequiredMixin, DeleteView):
    model = Taolu
    success_url = '/taolu/'
    template_name = 'taolu/taolu-delete.html'


class SearchResultsView(ListView):
    model = Taolu
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Taolu.objects.filter(
            Q(name__icontains=query)
        )
        return object_list



@login_required
def create(request):
   form = TaoluForm()
   error =' '
   if request.method =='POST':
       form = TaoluForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect ('create')

       else:
           error = 'Заповніть коректно поле'



   #form = TaoluForm()
   context = {
       'form': form,
       'error': error
   }


   return render(request, 'taolu/create.html', context)

