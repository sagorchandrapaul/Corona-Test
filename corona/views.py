from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .forms import PatientForm
from .models import Patient


def index(request):
    template = 'patient/index.html'
    form = PatientForm(request.POST or None)
    patient = Patient()
    if request.method == 'POST':
        if form.is_valid():
            age = form.cleaned_data.get('age')
            gender = form.cleaned_data.get('gender')
            temperature = form.cleaned_data.get('temperature')
            symptoms = form.cleaned_data.get('symptoms')
            additionalInformation = form.cleaned_data.get('additionalInformation')

            score = 0
            count = 0
            count1 = 0
            stepcount = 3
            sys = ['BP','DC', 'ST', 'W', 'RN']
            others = ['AP', 'V', 'D', 'CP', 'P', 'MP', 'LT','LS', 'RS', 'DF','DT','LS','LM']
            if (temperature >= 99.5 or temperature <= 100.9):
                score += 2
            if (len(symptoms) != 0):
                for i in sys:
                    for j in symptoms:
                        if i == j:
                            count += 1
                score += (count / count) * (count + (stepcount - 1))
            score = int(score)
            print(score)
            if (len(additionalInformation) != 0):
                count1 = 0
                for i in others:
                    for j in additionalInformation:
                        if i == j:
                            count1 += 1
                count1 = count1 * 2
            score += count1
            print(score)
            p = Patient.objects.create(age=age, gender=gender, score=score,
                                           temperature=temperature, symptoms=symptoms,
                                           additionalInformation=additionalInformation)
            print(p.pk)
            return HttpResponseRedirect(reverse('corona:detail', args=(p.id,)))
        else:
            return render(request, template, {'form': form})
    context = {
        'form': form,
    }
    return render(request, template, context)

  

class PatientListView(ListView):
    template_name = "patient/result.html" # Default: <app_label>/<model_name>_list.html
    queryset = Patient.objects.all().order_by('-id')
    context_object_name = 'patient' # Default: object_list
    paginate_by = 10



def detail(request, id):
    template = 'patient/detail.html'
    patient = get_object_or_404(Patient, pk=id)
    context = {
        'patient': patient
    }
    return render(request, template, context)

