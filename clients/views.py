from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog
from clients.models import Clients
from pytils.translit import slugify

from mailing.models import Mailing


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


class BlogView(ListView):
    template_name = 'clients/main.html'
    model = Blog
    context_object_name = 'blog_objects'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_list'] = Clients.objects.values('name', 'email', 'creation_date').distinct()
        context['mailing'] = Mailing.objects.values('subject', 'status')
        context['mailing_status'] = Mailing.objects.values('subject', 'status').filter(status__in=['created', 'started'])
        return context

    def get_queryset(self):
        all_blog_objects = Blog.objects.all()
        return sample(list(all_blog_objects), 3)


class View_blogDetailView(DetailView):
    model = Blog
    template_name = 'clients/view_blog_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_num += 1
        obj.save()
        return obj
