from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .forms import guestsForm
from .models import guests_registration
from rest_framework import viewsets
from .serializers import GuestSerializers


def register_guest(request):
    form = guestsForm()
    if request.method == 'POST':
        form = guestsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('register') 
    context = {"form": form}
    return render(request, 'home.html', context)
@login_required
def dashboard_view(request):
    all_guests = guests_registration.objects.all().order_by('-date_recorded')
    context = {'all_guests': all_guests} 
    return render(request, 'dashboard.html', context)


class GuestUpdateView(UpdateView):
    model = guests_registration
    form_class = guestsForm
    template_name = "guest_update.html"
    success_url = reverse_lazy('dashboard')


class GuestDeleteView(DeleteView):
    model = guests_registration
    template_name = "guest_delete.html" 
    success_url = reverse_lazy('dashboard')


class GuestDetailView(DetailView):
    model = guests_registration
    template_name = "guest_detail.html"
    context_object_name = 'guest'
    

class GuestCreateView(CreateView):
    model = guests_registration
    form_class = guestsForm
    template_name = "guest_create.html"
    success_url = reverse_lazy('dashboard')


    class GuestViewSet(viewsets.ModelViewSet):
        queryset = guests_registration.objects.all()
        serializer_class = GuestSerializer
