# Createfrom django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Conteudoprog, Cronograma
from .forms import CronogramaForm, ConteudoprogForm



def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')    

# lista de cronogramas ensino médio
@login_required 
def meuscronogramas(request):
    tasks_list = Cronograma.objects.all().filter(user=request.user)
    paginator = Paginator(tasks_list, 3)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

    return render(request, 'meuscronogramas.html', {'tasks' : tasks})

#exibir tarefa ensino médio
@login_required   
def cronogramaview(request, id):
    cronograma = get_object_or_404(Cronograma, pk=id)
    return render(request, 'tarefa.html', {'cronograma': cronograma} )

# adicionar cronograma ensino médio
@login_required 
def novocronograma(request):
    if request.method == 'POST':
        form = CronogramaForm(request.POST)
        if form.is_valid():
            cronograma = form.save(commit=False)
            cronograma.done = "doing"
            cronograma.user = request.user
            cronograma.save()
            return redirect('meuscronogramas')
    else:        
        form = CronogramaForm()
        return render(request, 'adicionar.html', {'form': form})

# editar tarefa ensino médio
@login_required 
def editcron(request, id):
    cronograma = get_object_or_404(Cronograma, pk=id)
    form = CronogramaForm(instance=cronograma)
    
    if(request.method == 'POST'):
        form = CronogramaForm(request.POST, instance=cronograma)
        if (form.is_valid()):
            cronograma.save()
            return redirect('meuscronogramas')
        else:
            return render(request, 'editartarefa.html', {'form': form, 'cronograma': cronograma})
    else: 
        return render(request, 'editartarefa.html', {'form': form, 'cronograma': cronograma})

# concluir tarefa ensino médio
@login_required        
def donecron(request, id):
    cronograma = get_object_or_404(Cronograma, pk=id)
    if(request.method == 'GET'):
    
       if(cronograma.done == 'doing'):
           cronograma.done = 'done'
       else: 
           cronograma.done = 'doing'
       cronograma.save()
       return redirect ('meuscronogramas')
   # if(request.method == 'GET'):
       # return redirect('meuscronogramas')

# deletar tarefa ensino médio
@login_required 
def deletecron(request, id):
    cronograma = get_object_or_404(Cronograma, pk=id)
    cronograma.delete()

    if(request.method == 'GET'):
      return redirect('meuscronogramas')

    else:
      return redirect('/')




# CONCURSO PUBLICO E VESTIBULAR

# lista de conteúdo progmático concurso/vestib
@login_required 
def cronogramasconc(request):
    tasks_list = Conteudoprog.objects.all().filter(user=request.user)
    paginator = Paginator(tasks_list, 3)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, 'concursos/cronogramasconc.html', {'tasks' : tasks})

#exibir conteudo progmático concurso/vestib após clicar
@login_required   
def conteudoprogview(request, id):
    conteudoprog = get_object_or_404(Conteudoprog, pk=id)
    return render(request, 'concursos/conteudoprogmatico.html', {'conteudoprog': conteudoprog})

# adicionar conteudo progmático concursovestib
 
@login_required 
def newvestib(request):
    if request.method == 'POST':
            form = ConteudoprogForm(request.POST)
            if form.is_valid():
             conteudoprog = form.save(commit=False)
             conteudoprog.done = "doing"
             conteudoprog.user = request.user
             conteudoprog.save()

            return redirect('cronogramasconcurso')
    else:        
        form = ConteudoprogForm()
        return render(request, 'concursos/addconcurso.html', {'form': form})

# editar conteudo progmatico vestibular/concurso
@login_required 
def editcronvest(request, id):
    conteudoprog = get_object_or_404(Conteudoprog, pk=id)
    form = ConteudoprogForm(instance=conteudoprog)
    
    if(request.method == 'POST'):
        form = CronogramaForm(request.POST, instance=conteudoprog)
        if (form.is_valid()):
            conteudoprog.save()
            return redirect('concursos/processoseletivo')
        else:
            return render(request, 'concursos/editarconcurso.html', {'form': form, 'conteudoprog': conteudoprog})
    else: 
        return render(request, 'concursos/editarconcurso.html', {'form': form, 'conteudoprog': conteudoprog})


# deletar concurso/vestib
@login_required 
def deletecronvest(request, id):
    conteudoprog = get_object_or_404(Conteudoprog, pk=id)
    conteudoprog.delete()

    if(request.method == 'GET'):
      return redirect('concursos/processoseletivo')

    else:
      return redirect('/')

def processoseletivo(request):
    return render(request, 'concursos/processoseletivo.html')    