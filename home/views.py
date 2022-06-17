from django.shortcuts import render


# Create your views here.

pickle_list=[{'id':1, 'page':'Mango'},{'id':2, 'page':'Radish'},{'id':3, 'page':'B/amboo'}]

def homepage(requests):
    context = {'pickles':pickle_list}
    return render(requests,'home.html', context)

def otherpages(request,pk):
    for i in pickle_list:
        if i['id'] == pk:
            page = i 
    context = page
    return render(request, 'indipickles.html',context)


