from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import CommentForm
from .models import *


# Начальная страница
def start(request):
    sections = Section.objects.all()
    new_receipts = CountryReceipt.objects.all().order_by('-time_creation')[0:5]
    new_comments = CountryComment.objects.all().order_by('-time_creation')[0:5]
    return render(request, 'country/start.html', {'sections': sections,
                                                  'new_receipts': new_receipts,
                                                  'new_comments': new_comments})


# Список стран
class ListOfCountries(ListView):
    model = Country
    ordering = ['title']
    template_name = 'country/countries.html'
    context_object_name = 'countries'
    paginate_by = 15


# Просмотр страны
class CountryDetail(DetailView):
    model = Country
    template_name = 'country/country_view.html'
    context_object_name = 'country_view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_receipt'] = CountryReceipt.objects.filter(country=self.object.id)
        return context


# Страница рецепта
class Receipt(DetailView):
    model = CountryReceipt
    template_name = 'country/receipt_view.html'
    context_object_name = 'receipt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CountryComment.objects.filter(receipt__exact=self.object.id).order_by('-time_creation')
        return context

    def post(self, request, **kwargs):
        comment = CountryComment()
        receipt = CountryReceipt.objects.get(id=self.kwargs.get('pk'))
        comment.text = self.request.POST.get("text")
        comment.author = self.request.user
        comment.receipt = receipt
        comment.save()
        return HttpResponseRedirect(receipt.get_absolute_url())


# Редактирование комментария
class CommentUpdate(LoginRequiredMixin, UpdateView):
    form_class = CommentForm
    model = CountryComment
    template_name = 'country/comment_edit.html'
    success_url = reverse_lazy('receipts_country')


# Удаление комментария
class CommentDelete(LoginRequiredMixin, DeleteView):
    model = CountryComment
    template_name = 'country/comment_delete.html'
    success_url = reverse_lazy('receipts_country')


# Список рецептов для ссылки "рецепты"
class ListOfReceipts(ListView):
    model = CountryReceipt
    ordering = ['time_creation']
    template_name = 'country/receipt_list.html'
    context_object_name = 'receipt_list'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        if self.request.GET:
            if "section" in self.request.GET and self.request.GET.get("section"):
                section = self.request.GET.get("section")
                receipts = CountryReceipt.objects.filter(section=section).order_by('-time_creation')
            else:
                receipts = CountryReceipt.objects.all().order_by('-time_creation')
            return receipts
        else:
            return CountryReceipt.objects.all().order_by('-time_creation')
