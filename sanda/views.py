from urllib import request
from django.shortcuts import render, redirect
from .models import Sanda
from .forms import SandaForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def sanda(request):
    sanda = Sanda.objects.order_by('name')
    paginator = Paginator(sanda, 3)
    page_number = request.GET.get('page')
    sanda = paginator.get_page(page_number)
    return render(request, 'sanda/sanda.html', {'sanda': sanda})
   # sanda = Sanda.objects.order_by('name')
   # return render(request, 'sanda/sanda.html', {'sanda':sanda})

class SandaDetailView(LoginRequiredMixin, DetailView):
    model = Sanda
    template_name ='sanda/sandadetails_view.html'
    context_object_name = 'sanda'


class SandaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sanda
    template_name = 'sanda/sandacreate.html'

    form_class = SandaForm


class SandaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sanda
    success_url = '/sanda/'
    template_name = 'sanda/sanda-delete.html'


class SearchResultsView(ListView):
    model = Sanda
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Sanda.objects.filter(
            Q(name__icontains=query)
        )
        return object_list




@login_required
def sandacreate(request):
   form = SandaForm()
   error =' '
   if request.method =='POST':
       form = SandaForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect ('sandacreate')

       else:
           error = 'Заповніть коректно поле'



   #form = TaoluForm()
   context = {
       'form': form,
       'error': error
   }


   return render(request, 'sanda/sandacreate.html', context)

