from django.views.generic import View
from django.shortcuts import render

class CalculadoraView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {"lista":[1,2,3,4,5]})
    
    def post(self, request, *args, **kwargs):
        pass