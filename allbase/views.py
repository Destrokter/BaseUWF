from urllib import request
from django.shortcuts import render, redirect
from .models import Allbase
from .forms import AllbaseForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#from allbase.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def allbase(request):
    allbase = Allbase.objects.order_by('name')
    paginator = Paginator(allbase, 3)
    page_number = request.GET.get('page')
    allbase = paginator.get_page(page_number)
    return render(request, 'allbase/allbase.html', {'allbase': allbase})

class AllbaseDetailView(LoginRequiredMixin, DetailView):
    model = Allbase
    template_name ='allbase/allbasedetails_view.html'
    context_object_name = 'allbase'


class AllbaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Allbase
    template_name = 'allbase/allbasecreate.html'

    form_class = AllbaseForm


class AllbaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Allbase
    success_url = '/allbase/'
    template_name = 'allbase/allbase-delete.html'


class SearchResultsView(ListView):
    model = Allbase
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Allbase.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

@login_required
def allbasecreate(request):
   form = AllbaseForm()
   error =' '
   if request.method =='POST':
       form = AllbaseForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect ('allbasecreate')

       else:
           error = 'Заповніть коректно поле'



   #form = TaoluForm()
   context = {
       'form': form,
       'error': error
   }


   return render(request, 'allbase/allbasecreate.html', context)