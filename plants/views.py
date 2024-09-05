from django.shortcuts import render, redirect
from .models import Plant

def plant_list(request):
    plants = Plant.objects.all()
    context = {'plants': plants}
    return render(request, 'plants/plant_list.html', context)

def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            return redirect('plant_detail', plant.pk)
    else:
        form = PlantForm()
    return render(request, 'plants/plant_create.html', {'form': form})

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plants/plant_detail.html', {'plant': plant})
