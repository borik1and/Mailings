from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from users.models import Users
from pytils.translit import slugify


class UsersCreateView(CreateView):
    model = Users
    fields = ('name', 'father_name', 'surname', 'comments', 'email')
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user:list')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            new_user.slug = slugify(new_user.name)
            new_user.save()

        return super().form_valid(form)


class UsersListView(ListView):
    model = Users

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(publication=True)
    #     return queryset


class UsersDetailView(DetailView):
    model = Users

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     obj.view_num += 1
    #     obj.save()
    #     return obj


class UsersUpdateView(UpdateView):
    model = Users
    fields = ('name', 'father_name', 'surname', 'comments', 'email')
    template_name = 'users/users_form.html'
    success_url = reverse_lazy('users:list')
    queryset = Users.objects.all()

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            new_user.slug = slugify(new_user.name)
            new_user.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:view', args=[self.kwargs.get('pk')])


class UsersDeleteView(DeleteView):
    model = Users
    success_url = reverse_lazy('clients:list')

