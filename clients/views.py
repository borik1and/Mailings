from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog
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


class ClientsListView(LoginRequiredMixin, ListView):
    model = Clients
    template_name = 'clients/clients_list.html'
    context_object_name = 'client_list'


class ClientsDetailView(DetailView):
    model = Clients


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
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


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:list')


def blog_view(request):
    all_blog_objects = Blog.objects.all()
    random_blog_objects = sample(list(all_blog_objects), 3)
    return render(request, 'clients/main.html', {'blog_objects': random_blog_objects})


class View_blogDetailView(DetailView):
    model = Blog
    template_name = 'clients/view_blog_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_num += 1
        obj.save()
        return obj
