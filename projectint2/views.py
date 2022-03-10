# Createfrom django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Cronograma
from .forms import CronogramaForm



def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')    

# lista de cronogramas
@login_required 
def meuscronogramas(request):
    tasks_list = Cronograma.objects.all().filter(user=request.user)
    paginator = Paginator(tasks_list, 3)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

    return render(request, 'meuscronogramas.html', {'tasks' : tasks})

#exibir tarefa
@login_required   
def cronogramaview(request, id):
    cronograma = get_object_or_404(Cronograma, pk=id)
    return render(request, 'tarefa.html', {'cronograma': cronograma} )

# adicionar cronograma
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

# editar tarefa
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

# concluir tarefa
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

# deletar tarefa
@login_required 
def deletecron(request, id):
    cronograma = get_object_or_404(Cronograma, pk=id)
    cronograma.delete()

    if(request.method == 'GET'):
      return redirect('meuscronogramas')

    else:
      return redirect('/')