from django.shortcuts import render, redirect
from django.db import transaction 
from django.views import View
from django.contrib import messages
from admin_setori.models import *

class Master_sliderViews(View):
    def get(self, request):
        return render(request, 'admin/master_slider/index.html')
    
class Addslider(View):
    def get(self, request):
        return render(request, 'admin/master_slider/form.html')
    
    def post(self, request):
        logo = request.FILES.get('logo')
        foto = request.FILES.get('foto')
        judul = request.POST.get('judul')
        try:
            with transaction.atomic():
                table = slider()
                table.logo = logo
                table.foto = foto
                table.judul = judul
                table.save()
                messages.success(request, f"kategori berhasil ditambahkan")
                return redirect('admin_setori:master_slider')
        except Exception as e:
            print('Error Data')
           

