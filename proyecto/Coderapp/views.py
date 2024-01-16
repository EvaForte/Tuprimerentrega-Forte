from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "Coderapp/index.html")


def coordinador_list(request):
    consulta = models.Coordinador.objects.all()
    contexto = {"coordinadores": consulta}
    return render(request, "Coderapp/coordinador_list.html", contexto)

def coordinador_form(request):
    if request.method == "POST":
        form = forms.CoordinadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("coordinador_list")
    else:
        form = forms.CoordinadorForm()
    return render(request, "Coderapp/coordinador_form.html", {"form": form})