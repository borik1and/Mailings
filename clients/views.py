from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from clients.models import Clients
from pytils.translit import slugify


class ClientsCreateView(CreateView):
    model = Clients
    fields = ('name', 'father_name', 'surname', 'comments', 'email')
    template_name = 'clients/clients_form.html'
    success_url = reverse_lazy('clients:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class ClientsListView(ListView):
    model = Clients

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(publication=True)
    #     return queryset


class ClientsDetailView(DetailView):
    model = Clients

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     obj.view_num += 1
    #     obj.save()
    #     return obj


class ClientsUpdateView(UpdateView):
    model = Clients
    fields = ('name', 'father_name', 'surname', 'comments', 'email')
    template_name = 'clients/clients_form.html'
    success_url = reverse_lazy('clients:list')
    queryset = Clients.objects.all()

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('clients:view', args=[self.kwargs.get('pk')])


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:list')
