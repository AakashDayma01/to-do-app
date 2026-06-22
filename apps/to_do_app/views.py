from django.shortcuts import render,get_object_or_404 ,redirect

# Create your views here.
from .models import Task

def add_task(request):
    if request.method == "POST":
        task_text = request.POST.get('text') 
        if not task_text or task_text.strip() == "":
            all_tasks = Task.objects.all()
            return render(request, 'home.html', {
                'tasks': all_tasks, 
                'error_message': "You didn't enter any task."
            })
            
        Task.objects.create(title=task_text)
        return redirect('home')

    all_tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': all_tasks})


def delete_task(request, id):
	if request.method == "POST":
		task = get_object_or_404(Task, pk=id)
		task.delete()
	return redirect('home')

def update_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.title = request.POST.get('updated_text') 
        task.save()
    return redirect('home') # Replace with your home page URL name

