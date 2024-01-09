from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from django.core.management import call_command
from mailing.models import Mailing, EmailLog


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    fields = ('subject', 'mailing_start_time', 'mailing_stop_time', 'period', 'status', 'content')
    permission_required = 'mailing.add_mailing'
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save(commit=False)
            new_mailing.slug = slugify(new_mailing.subject)
            new_mailing.owner = self.request.user  # Установите владельца текущим пользователем
            new_mailing.save()
            call_command('send_emails')

        return super().form_valid(form)


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing


def mailing_log(request):
    logs = EmailLog.objects.all()
    return render(request, 'mailing/mailing_loglist.html', {'logs': logs})


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    permission_required = 'mailing.detail_mailing'

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     obj.view_num += 1
    #     obj.save()
    #     return obj


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    fields = ('subject', 'mailing_start_time', 'mailing_stop_time', 'period', 'status', 'content')
    permission_required = 'mailing.change_mailing'
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


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.delete_mailing'
