# python library imports
from datetime import date
# django library imports
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
# my apps imports
from apps.lectura.models import MeterReading
# Create your views here.


def home(request):
    # establishment_list = Establishment.objects.all()
    context = {}
    return render(request, 'home.html', context)


class MeterReadingList(LoginRequiredMixin, ListView):
    model = MeterReading
    paginate_by = 100  # if pagination is desired
    template_name = "lectura/meterreading_list.html"

    def get_queryset(self):
        new_context = MeterReading.objects.filter(user_id = self.request.user).order_by('reading_date')
        return new_context


class MeterReadingCreate(LoginRequiredMixin, CreateView):
    model = MeterReading
    fields = ['contract_number', 'commercial_office_id', 'route', 'number', 'reading']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        # form.instance.reading_date = date.today
        return super().form_valid(form)


# class MeterReadingUpdate(UpdateView):
#     model = MeterReading
#     fields = ['contract_number']
#

class MeterReadingDelete(LoginRequiredMixin, DeleteView):
    model = MeterReading
    success_url = reverse_lazy('author-list')