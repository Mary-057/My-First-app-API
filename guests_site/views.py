from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .forms import guestsForm
from .models import guests_registration

# --- Function-Based Views (FBV) ---
def register_guest(request):
    form = guestsForm()
    if request.method == 'POST':
        form = guestsForm(request.POST)
        if form.is_valid():
            form.save()
            # FIX: We use redirect to the clean form page after a successful save.
            return redirect('register') 
        
    # FIX: This renders the form with any errors if validation failed (on POST) or displays a blank form (on GET).
    context = {"form": form}
    return render(request, 'home.html', context)
@login_required
def dashboard_view(request):
    all_guests = guests_registration.objects.all().order_by('-date_recorded')
    context = {'all_guests': all_guests} 
    return render(request, 'dashboard.html', context)


# --- Class-Based Views (CBVs) ---
# NOTE: The definition with 'class' makes these objects valid for .as_view()

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