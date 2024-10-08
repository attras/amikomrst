from django.shortcuts import render, redirect
from django.db import transaction 
from django.views import View

from admin_setori.models import *

class Admin_kontakViews(View):
    def get(self, request):
        dt_kontak = Admin_kontak.objects.filter(delete_at__isnull = True)
        data = {
            'dt_kontak' : dt_kontak
        }
        return render(request, 'admin/admin_kontak/index.html',data)
    
class Addkontak(View) :
    def post(self, request):
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        alamat = request.POST.get('alamat')
        jam_kerja = request.POST.get('jam_kerja')
        try:
            table = Admin_kontak()
            table.email = email
            table.phone = phone
            table.alamat = alamat
            table.jam_kerja = jam_kerja
            table.create_at = timezone.now()
            table.save()
            return redirect('admin_setori:master_kategori')
        except Exception as e:
            print('Error Data')
            return redirect('admin_setori:master_kategori')