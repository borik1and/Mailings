from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from users.models import Users
from pytils.translit import slugify


class MailingCreateView(CreateView):
    model = Users
    fields = ('mailing_start_time', 'mailing_stop_time', 'period', 'status', 'message')
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.slug = slugify(new_mailing.name)
            new_mailing.save()

        return super().form_valid(form)


class MailingListView(ListView):
    model = Users

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(publication=True)
    #     return queryset


class MailingDetailView(DetailView):
    model = Users

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     obj.view_num += 1
    #     obj.save()
    #     return obj


class MailingUpdateView(UpdateView):
    model = Users
    fields = ('mailing_start_time', 'mailing_stop_time', 'period', 'status', 'message')
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:list')
    queryset = Users.objects.all()

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.slug = slugify(new_mailing.name)
            new_mailing.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailing:view', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Users
    success_url = reverse_lazy('mailing:list')
