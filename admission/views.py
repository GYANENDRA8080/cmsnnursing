from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionForm, HostelForm


def admission_view(request):
    form = AdmissionForm()
    hostel_form = HostelForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type', 'admission')
        if form_type == 'hostel':
            hostel_form = HostelForm(request.POST)
            if hostel_form.is_valid():
                hostel_form.save()
                messages.success(request, 'Hostel admission enquiry submitted successfully! We will contact you soon.')
                return redirect('admission:admission')
        else:
            form = AdmissionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Admission enquiry submitted successfully! We will contact you soon.')
                return redirect('admission:admission')

    context = {
        'form': form,
        'hostel_form': hostel_form,
    }
    return render(request, 'admission/admission.html', context)
