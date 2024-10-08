from django.shortcuts import render, redirect
from django.db import transaction 
from django.views import View
from django.contrib import messages
from admin_setori.models import *

class Master_kategoriViews(View):
    def get(self, request):
        dt_kategori = Kategori_berita.objects.filter(delete_at__isnull = True,)
        data = {
            'dt_kategori' : dt_kategori
        }
        return render(request, 'admin/master_kategori/index.html',data)
    
class Addkategori(View) :
    def post(self, request):
        kategori = request.POST.get('kategori')
        try:
            with transaction.atomic():
                table = Kategori_berita()
                table.nama_kategori = kategori
                table.create_at = timezone.now()
                table.save()

                messages.success(request, f"kategori berhasil ditambahkan")
                return redirect('admin_setori:master_kategori')
        except Exception as e:
            print('Error Data')
            return redirect('admin_setori:master_kategori')
