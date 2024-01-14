from django.shortcuts import render

# Create your views here.

# Create function
def template_view(request):
    #create dictionary to pass
    #data to the template
    context ={
        "data": "Magheswari",
        "class": "MCA",
        "address": "Mumbai",
        
    }
    #return response with template and context
    return render(request, "myapp/base.html", context)