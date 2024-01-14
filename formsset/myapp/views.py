from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render
from django.forms import modelformset_factory
from .models import MyModel
from .forms import MyModelForm

def my_view(request):
    MyModelFormSet = modelformset_factory(MyModel, form=MyModelForm, extra=2)  # Set 'extra' as per your requirement
    if request.method == 'POST':
        formset = MyModelFormSet(request.POST, queryset=MyModel.objects.none())
        if formset.is_valid():
            formset.save()
    else:
        formset = MyModelFormSet(queryset=MyModel.objects.none())
    return render(request, 'myapp/my_template.html', {'formset': formset})