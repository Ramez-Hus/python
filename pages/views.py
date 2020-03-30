from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from .forms import ListForm

from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


# Create your views here.
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("YB home, Django!")
# def about(request):
#     return HttpResponse("YB about, Django!")

def home(request):
    return render(request,"home.html",{})
def about(request):
    context = {'first_name': 'Yousef', 'last_name': 'Ballan'}
    return render(request, "about.html",context)


# def todo(request):
#     return HttpResponse("YB ToDo App!")


# def todo(request):
#     all_items = List.objects.all
#     return render(request, "todo.html",{'all_items':all_items})

# def todo(request):
# 	if request.method == 'POST':
# 		form = ListForm(request.POST or None)
        
# 		if form.is_valid():
# 			form.save()
# 			all_items = List.objects.all
# 			return render(request, 'todo.html', {'all_items': all_items})

# 	else:
# 		all_items = List.objects.all
# 		return render(request, 'todo.html', {'all_items': all_items})

def todo(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
        
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('Item Has Been Added To List!'))
			return render(request, 'todo.html', {'all_items': all_items})
	else:
		all_items = List.objects.all
		return render(request, 'todo.html', {'all_items': all_items})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect('todo')


def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('todo')	

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('todo')	

def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)

		form = ListForm(request.POST or None, instance=item)
		#form = ListForm(request.POST or None) #working
        
		if form.is_valid():
			form.save()
			messages.success(request, ('Item Has Been Edited!'))
			return redirect('todo')

	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})
