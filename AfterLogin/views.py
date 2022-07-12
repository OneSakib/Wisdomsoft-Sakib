from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, FormView, View
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Index(ListView, FormView):
    template_name = 'index.html'
    model = Car
    form_class = CarForm

    def post(self, request):
        form = CarForm(request.POST)
        type = request.POST.get('type')
        if type == 'create':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('afterlogin:index'))
        elif type == 'delete':
            pk = request.POST.get('pk')
            obj = Car.objects.get(pk=pk)
            obj.delete()
            return HttpResponseRedirect(reverse_lazy('afterlogin:index'))
        return HttpResponseRedirect(reverse_lazy('afterlogin:index'))


@method_decorator(login_required, name='dispatch')
class CarUpdate(View):

    def get(self, request, pk):
        car_obj = Car.objects.get(pk=pk)
        pk = pk
        form = CarForm(instance=car_obj)
        context = {
            'form': form
        }
        return render(request, 'update.html', context)

    def post(self, request, pk):
        car_obj = Car.objects.get(pk=pk)
        form = CarForm(instance=car_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('afterlogin:index'))
        return HttpResponseRedirect(reverse_lazy('afterlogin:index'))
