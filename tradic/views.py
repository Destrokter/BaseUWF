from urllib import request
from django.shortcuts import render, redirect
from .models import Tradic
from .forms import TradicForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def tradic(request):
    tradic = Tradic.objects.order_by('name')
    paginator = Paginator(tradic, 3)
    page_number = request.GET.get('page')
    tradic = paginator.get_page(page_number)
    return render(request, 'tradic/tradic.html', {'tradic': tradic})
    #tradic = Tradic.objects.order_by('name')
    #return render(request, 'tradic/tradic.html', {'tradic':tradic})

class TradicDetailView(LoginRequiredMixin, DetailView):
    model = Tradic
    template_name ='tradic/tradicdetails_view.html'
    context_object_name = 'tradic'


class TradicUpdateView(LoginRequiredMixin, UpdateView):
    model = Tradic
    template_name = 'tradic/tradiccreate.html'

    form_class = TradicForm


class TradicDeleteView(LoginRequiredMixin, DeleteView):
    model = Tradic
    success_url = '/tradic/'
    template_name = 'tradic/tradic-delete.html'


class SearchResultsView(ListView):
    model = Tradic
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Tradic.objects.filter(
            Q(name__icontains=query)
        )
        return object_list




@login_required
def tradiccreate(request):
   form = TradicForm()
   error =' '
   if request.method =='POST':
       form = TradicForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect ('tradiccreate')

       else:
           error = 'Заповніть коректно поле'



   #form = TaoluForm()
   context = {
       'form': form,
       'error': error
   }


   return render(request, 'tradic/tradiccreate.html', context)

