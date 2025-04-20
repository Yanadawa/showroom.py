from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Service
from .forms import CarForm, ServiceForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# List to all cars
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'showroom/car_list.html', {'cars': cars})

# Details for a specific car
def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    services = car.services.all()

    # default values
    total_biaya_servis = sum(service.biaya for service in services)
    hpp = None
    cicilan_bulanan = None

    if car.pinjaman_bank and car.suku_bunga:
        total_pinjaman = car.pinjaman_bank * (1 + (car.suku_bunga / 100))
        cicilan_bulanan = total_pinjaman / 12
        hpp = (car.harga_dasar / total_pinjaman) + total_biaya_servis
    else:
        cicilan_bulanan = 0
        hpp = car.harga_dasar + total_biaya_servis

    context = {
        'car' : car,
        'services' : services,
        'total_biaya_servis' : total_biaya_servis,
        'cicilan_bulanan' : cicilan_bulanan,
        'hpp' : hpp,
    }

    return render(request, 'showroom/car_detail.html', context)

# Add a new car
def car_add(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)

            # if car isn't loaned by bank, delete  loan and interest
            if not form.cleaned_data.get('dibiayai_bank'):
                car.pinjaman_bank = None
                car.suku_bunga = None

            car.save()
            return redirect('car_list')
        
    else:
        form = CarForm()
    return render(request, 'showroom/car_form.html', {'form': form})

# Add a service to a car
def service_add(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            service = form.save(commit=False)
            service.mobil = car # link to the selected car
            service.save()
            return redirect('car_detail', car_id=car.id) # redirect to car detail page
            
        else:
            print(form.errors)

    else:
        form = ServiceForm()
    return render(request, 'showroom/service_form.html', {'form': form, 'car': car})

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'showroom/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')