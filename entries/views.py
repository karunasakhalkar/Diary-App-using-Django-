from django.shortcuts import render,redirect
from .models import Entry
from .forms import EntryForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    entries = Entry.objects.order_by('-date_posted')
    paginator=Paginator(entries,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)


    ttext=request.GET.get('ttext')
    if ttext!='' and ttext is not None:
        page_obj=doc_list.filter(text__contains=ttext)





    my_dict={'page_obj':page_obj}
    return render(request,'entries/index.html',my_dict)

    # context = {'entries': entries}
    # return render(request,'entries/index.html',context)


def add(request):
    if request.method == 'POST':
        form=EntryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            form=EntryForm()


    form=EntryForm()

    context = {'form' : form}

    
    return render(request,'entries/add.html',context)
    