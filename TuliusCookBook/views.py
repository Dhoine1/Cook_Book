from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count, F
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
import random

from .models import *
from .forms import ReceiptForm, CommentForm


def start(request):
    new_receipts = Recipe.objects.all().order_by('-time_creation')[0:5]
    new_comments = Comment.objects.all().order_by('-time_creation')[0:5]
    count = Fact.objects.all().count()
    random_number = random.randint(0, count - 1)
    useless_fact = Fact.objects.all()[random_number]
    sections = Section.objects.all()
    return render(request, 'tuliuscookbook/start.html', {'new_receipts': new_receipts,
                                                         'new_comments': new_comments,
                                                         'useless_fact': useless_fact,
                                                         'sections': sections})


# Список сюжетов для ссылки "игры"
class ListOfGame(ListView):
    model = CatalogStories
    ordering = ['title']
    template_name = 'tuliuscookbook/games.html'
    context_object_name = 'games'
    paginate_by = 20

    def get_queryset(self, **kwargs):
        if self.request.GET:
            if "story" in self.request.GET and self.request.GET.get("story"):
                story = self.request.GET.get("story")
                stories = CatalogStories.objects.filter(Q(title__iregex=story)).annotate(number=Count('recipe')).order_by('title')
                return stories
            elif "sort_by" in self.request.GET:
                sort_by = self.request.GET.get("sort_by")
                if sort_by == "title":
                    sort = 'title'
                elif sort_by == "receipts_count":
                    sort = '-number'
                return CatalogStories.objects.all().annotate(number=Count('recipe')).order_by(sort)
        return CatalogStories.objects.all().annotate(number=Count('recipe')).order_by('title')


# Список рецептов для ссылки "рецепты по играм"
class ListOfReceipts(ListView):
    model = Recipe
    ordering = ['time_creation']
    template_name = 'tuliuscookbook/receipt_list.html'
    context_object_name = 'receipt_list'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        if self.request.GET:
            if "section" in self.request.GET and self.request.GET.get("section"):
                section = self.request.GET.get("section")
                receipts = Recipe.objects.filter(section=section).order_by('-time_creation')
            else:
                receipts = Recipe.objects.all().order_by('-time_creation')
            return receipts
        else:
            return Recipe.objects.all().order_by('-time_creation')


# Детальный просмотр конкретного сюжета
class StoryDetail(DetailView):
    model = CatalogStories
    template_name = 'tuliuscookbook/story_view.html'
    context_object_name = 'story_view'


# Детальный просмотр конкретного рецепта
class Receipt(DetailView):
    model = Recipe
    template_name = 'tuliuscookbook/receipt.html'
    context_object_name = "receipt"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(recipe__exact=self.object.id).order_by('-time_creation')
        return context

    def post(self, request, **kwargs):
        comment = Comment()
        receipt = Recipe.objects.get(id=self.kwargs.get('pk'))
        comment.text = self.request.POST.get("text")
        comment.author = self.request.user
        comment.recipe = receipt
        comment.save()
        return HttpResponseRedirect(receipt.get_absolute_url())


# Создание рецепта
class CreateReceipt(LoginRequiredMixin, CreateView):
    form_class = ReceiptForm
    model = Recipe
    template_name = 'tuliuscookbook/receipt_edit.html'
    success_url = '/tuliuscookbook/start/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories'] = CatalogStories.objects.all().order_by('title')
        return context


# Редактирование рецепта
class ReceiptUpdate(LoginRequiredMixin, UpdateView):
    form_class = ReceiptForm
    model = Recipe
    template_name = 'tuliuscookbook/receipt_edit.html'
    success_url = '/tuliuscookbook/start/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories'] = CatalogStories.objects.all().order_by('title')
        return context

    def get_object(self, *args, **kwargs):
        obj = super(ReceiptUpdate, self).get_object(*args, **kwargs)
        if not obj.author == self.request.user:
            raise Http404
        return obj


# Удаление рецепта
class ReceiptDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'tuliuscookbook/receipt_delete.html'
    success_url = reverse_lazy('start')


# Редактирование комментария
class CommentUpdate(LoginRequiredMixin, UpdateView):
    form_class = CommentForm
    model = Comment
    template_name = 'tuliuscookbook/comment_edit.html'
    success_url = reverse_lazy('receipts')


# Удаление комментария
class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'tuliuscookbook/comment_delete.html'
    success_url = reverse_lazy('receipts')


# Случайный факт
def fact(request):
    count = Fact.objects.all().count()
    random_number = random.randint(0, count-1)
    useless_fact = Fact.objects.all()[random_number]
    return render(request, 'tuliuscookbook/fact.html', {'fact_ru': useless_fact})
