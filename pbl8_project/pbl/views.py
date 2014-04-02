from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from pbl.models import Treatment

def view_treatment(request,slug):
  treatment = get_object_or_404(Treatment, slug=slug)
  return render(request, 'pbl/treatment.html', {'treatment': treatment, 
    'treatments': Treatment.objects.all()})
