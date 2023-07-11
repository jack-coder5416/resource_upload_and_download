from django.shortcuts import render, redirect
from .models import Material
from django.http import HttpResponse


def upload_material(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']
        material = Material(title=title, file=file)
        material.save()
        return redirect('material_list')
    return render(request, 'upload_material.html')

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'material_list.html', {'materials': materials})

def download_material(request, material_id):
    material = Material.objects.get(id=material_id)
    file = material.file
    response = HttpResponse(file, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=' + file.name
    return response