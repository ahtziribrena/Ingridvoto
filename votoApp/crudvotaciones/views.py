from django.shortcuts import render, redirect
from . models import Ciudadanos
from . forms import CiudadanosForm
from . models import Candidaturas
from . forms import CandidaturasForm
from . models import Votos
from . forms import VotosForm

def registrarciudadanos(request):
    if request.method=='POST':
        form= CiudadanosForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/enlistarciudadanos')
            except:
                pass
    else:
        form =CiudadanosForm()
        return render(request, 'registrarciudadanos.html', {'form': form})

def registrarcandidaturas(request):
    if request.method=='POST':
        form= CandidaturasForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/enlistarcandidaturas')
            except:
                pass
    else:
        form =CandidaturasForm()
        return render(request, 'registrarcandidaturas.html', {'form': form})
    
def registrarvotaciones(request):
    if request.method=='POST':
        form=VotosForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/enlistarvotos')
            except:
                pass
    else:
        form =VotosForm()
        return render(request, 'registrarvotaciones.html', {'form': form})
    

def enlistarcandidaturas(request):
    candidaturas = Candidaturas.objects.all()
    return render(request, 'enlistarcandidaturas.html', {'candidaturas': candidaturas})

def enlistarciudadanos(request):
    ciudadanos = Ciudadanos.objects.all()
    return render(request, 'enlistarciudadanos.html', {'ciudadanos': ciudadanos})

def enlistarvotos(request):
    votos = Votos.objects.all()
    return render(request, 'enlistarvotos.html', {'votos': votos})


def eliminarciudadano(request, id):
    print('id: ', id)
    ciudadanos =Ciudadanos.objects.get(id=id)
    ciudadanos.delete()
    return redirect ('/enlistarciudadanos')

def eliminarcandidatura(request, id):
    print('id: ', id)
    candidaturas =Candidaturas.objects.get(id=id)
    candidaturas.delete()
    return redirect ('/enlistarcandidaturas')

def editarciudadanos (request, id):
    ciudadanos =Ciudadanos.objects.get(id=id)
    form=CiudadanosForm(instance=ciudadanos)
    if request.method=='POST':
        form= CiudadanosForm(request.POST, instance=ciudadanos)
        if form.is_valid():
            try:
                form.save()
                return redirect('/enlistarciudadanos')
            except:
                pass
    context={
        'ciudadanos':ciudadanos,
        'form':form
    }
    return render(request,"editarciudadanos.html", context)

def editarcandidaturas (request, id):
    candidaturas =Candidaturas.objects.get(id=id)
    form=CandidaturasForm(instance=candidaturas)
    if request.method=='POST':
        form= CandidaturasForm(request.POST, instance=candidaturas)
        if form.is_valid():
            try:
                form.save()
                return redirect('/enlistarcandidaturas')
            except:
                pass
    context={
        'candidaturas':candidaturas,
        'form':form
    }
    return render(request,"editarcandidaturas.html", context)

def layouts (request):
    return render(request,"registrarciudadanos.html")
