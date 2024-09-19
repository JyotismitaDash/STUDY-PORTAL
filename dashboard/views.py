from django.shortcuts import render,redirect
from dashboard.models import *
from dashboard.forms import *
from django.contrib import messages
from django.views import generic
from pytube import *
#from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
#Notes_Section

def notes(request):
    if request.method=='POST':
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
            messages.success(request,f"Notes Added from {request.user.username} Successfully")
            return redirect('/notes')
            
        
    else:
        form=NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'notes.html',context)

def Delete_Notes(request,pk):
    notes=Notes.objects.get(id = pk)
    notes.delete()
    messages.warning(request,f"Notes deleted from {request.user.username} Successfully")
    return redirect('/notes')

class NotesDetailView (generic.DetailView) :
    model = Notes
    template_name = 'notes_detail.html' 

#Homework Section
def homework(request):
    if request.method=='POST':
        form=HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False
            except:
                finished=False
            homeworks=Homework(user=request.user,subject=request.POST['subject'],
            title=request.POST['title'],description=request.POST['description'],
            due=request.POST['due'],
            is_finished=finished)
            homeworks.save()
            messages.success(request,f"Homework Added from {request.user.username} Successfully")
            return redirect('/homework')
    else:
        form=HomeworkForm()
    homework=Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done=True
    else:
        homework_done=False
    context={'homeworks':homework,'homework_done':homework_done,'form':form}
    return render(request,'homework.html',context) 
def update_homework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished==True:
        homework.is_finished=False
    else:
        homework.is_finished=True
    homework.save()
    return redirect('homework')
def Delete_Homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    homework.delete()
    messages.warning(request, f"Homework deleted from {request.user.username} Successfully")
    return redirect('/homework')
#youtube section


def youtube(request):
    form = YoutubeForm()
    result_list = []  

    if request.method == 'POST':
        form = YoutubeForm(request.POST)
        text = request.POST['text']
        s = Search(text)  
        for video in s.results:  
            result_dict = {
                'input': text,
                'title': video.title,
                'link': video.watch_url,
                'channel': video.author,
                'views': video.views,
                'duration': video.length,
                'published': video.publish_date,
                'thumbnail': video.thumbnail_url,
            }
            desc = ''
            if video.description is not None:
                for line in video.description:
                    desc += line
            result_dict['description'] = desc
            result_list.append(result_dict)
        context = {
            'form': form,
            'results': result_list,
        }
        return render(request, 'youtube.html', context)

    context = {'form': form, 'result_list': result_list}
    return render(request, 'youtube.html', context)
def To_do(request):
    if request.method == 'POST':
        form=Todoform(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False
            except:
                finished=False
            todos=Todo(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            todos.save()
            messages.success(request,f"TODO Added from {request.user.username} Successfully")
            return redirect('/todo')
    else:    
        form=Todoform()
    todo=Todo.objects.filter(user=request.user)
    if len(todo)==0:
        todos_done=True
    else:
        todos_done=False
    context={
        'todos':todo,
        'form':form,
        'todos_done':todos_done
    }
    return render(request,'todo.html',context)
def update_todo(request,pk):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished==True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    todo.save()
    return render(request,'todo.html')

def delete_todo(request,pk):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    messages.warning(request, f"TODO deleted from {request.user.username} Successfully")
    return redirect('Todo')

        
