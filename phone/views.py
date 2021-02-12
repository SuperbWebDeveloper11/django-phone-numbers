from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.template.loader import render_to_string
# messages framework
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# class-based generic views
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# import models
from django.contrib.auth.models import User
from .models import Phone

class PhoneDatatable(TemplateView): 
    template_name = 'phone/phone/phone_datatable.html'

class PhoneList(ListView): 
    model = Phone
    template_name = 'phone/phone/phone_list.html'
    context_object_name = 'phone_list'
    paginate_by = 5


class PhoneDetail(DetailView): 
    model = Phone
    template_name = 'phone/phone/phone_detail.html'
    context_object_name = 'phone'


class PhoneCreate(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, CreateView): # create phone 
    model = Phone
    initial = {'office': 'office name', 'abbreviation': 'abrv', 'number': '123456'}
    template_name = 'phone/phone/phone_form_create.html' 
    fields = ['office', 'abbreviation', 'number']
    success_message = "phone was created successfully"
    permission_required = 'phone.add_phone'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)


class PhoneUpdate(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView): # update phone 
    model = Phone
    template_name = 'phone/phone/phone_form_update.html' 
    fields = ['office', 'abbreviation', 'number']
    success_message = "phone was updated successfully"
    permission_required = 'phone.change_phone'

    def form_valid(self, form):
        if form.instance.created_by == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse("you don't have permissions")

# delete phone 
class PhoneDelete(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Phone
    template_name = 'phone/phone/phone_confirm_delete.html' 
    success_message = "phone was deleted successfully"
    success_url = reverse_lazy('phone:phone_list')
    permission_required = 'phone.delete_phone'

    def form_valid(self, form):
        if form.instance.created_by == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse("you don't have permissions")


