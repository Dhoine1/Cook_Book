from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from TuliusCookBook.models import Profile, Recipe, Comment
from Country.models import CountryComment

from .forms import SignUpForm, ProfileForm


# Создание уч.записи
class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


# Создание профиля пользователя
class ProfileCreate(LoginRequiredMixin, CreateView):
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy('start')
    template_name = 'registration/profileupdate.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Изменение профиля пользователя
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'registration/profileupdate.html'
    raise_exception = True
    success_url = reverse_lazy('start')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receipt_list'] = Recipe.objects.filter(author=self.request.user.id).order_by('-time_creation')
        return context

    def get_object(self, *args, **kwargs):
        obj = super(ProfileUpdate, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj


# Список пользователей
class ListOfUser(LoginRequiredMixin, ListView):
    model = Profile
    ordering = ['nikname']
    template_name = 'registration/users.html'
    context_object_name = 'users'
    paginate_by = 20

    def get_queryset(self, **kwargs):
        if self.request.GET:
            if "author" in self.request.GET and self.request.GET.get("author"):
                author = self.request.GET.get("author")
                stories = User.objects.filter(Q(profile__nikname__iregex=author)).annotate(number=Count('recipe'))
                return stories
            elif "sort_by" in self.request.GET:
                sort_by = self.request.GET.get("sort_by")
                if sort_by == "nickname":
                    sort = 'profile__nikname'
                elif sort_by == "receipts_count":
                    sort = '-number'
                elif sort_by == "date":
                    sort = 'date_joined'
                return User.objects.all().annotate(number=Count('recipe')).order_by(sort)
        return User.objects.all().annotate(number=Count('recipe')).order_by('profile__nikname')


# Детальный просмотр конкретного профиля
class UserDetail(DetailView):
    model = Profile
    template_name = 'registration/user_view.html'
    context_object_name = 'user_view'


# Список моих комментариев
def mycomments(request):
    mycomments = Comment.objects.filter(author=request.user.id).order_by('-time_creation')
    return render(request, 'registration/comments.html', {'mycomments': mycomments})


# Список комментариев к моим рецептам
def comments_on_my_receiptes(request):
    mycomments = Comment.objects.filter(recipe__author=request.user.id).order_by('-time_creation')
    return render(request, 'registration/comments.html', {'mycomments': mycomments})


def mycomments_country(request):
    mycomments = CountryComment.objects.filter(author=request.user.id).order_by('-time_creation')
    return render(request, 'registration/comments_country.html', {'mycomments': mycomments})
