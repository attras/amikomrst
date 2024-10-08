from django.shortcuts import render, redirect

from django.views import View


class Master_wilayahViews(View):
    def get(self, request):
        return render(request, 'admin/master_wilayah/index.html')