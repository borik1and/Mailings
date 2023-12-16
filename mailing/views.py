# from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# from django.shortcuts import redirect
from pytils.translit import slugify
from django.core.management import call_command
from mailing.models import Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('subject', 'mailing_start_time', 'mailing_stop_time', 'period', 'status', 'content')
    # template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.slug = slugify(new_mailing.subject)
            new_mailing.save()
            call_command('send_emails')

        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     obj.view_num += 1
    #     obj.save()
    #     return obj


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('subject', 'mailing_start_time', 'mailing_stop_time', 'period', 'status', 'content')
    # template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:list')
    queryset = Mailing.objects.all()

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.slug = slugify(new_mailing.subject)
            new_mailing.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailing:view', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:list')
