from django.db import models

# Show all car models in showroom
class Car(models.Model):
    merk = models.CharField(max_length=100)  # Brand name
    model = models.CharField(max_length=100)  # Model name
    tahun = models.IntegerField()  # Car year
    harga_dasar = models.DecimalField(max_digits=12, decimal_places=2)

    # Bank field
    pinjaman_bank = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    suku_bunga = models.FloatField(null=True, blank=True)
    dibiayai_bank = models.BooleanField(default=False) # Toggle for boolean

    def __str__(self):
        return f"{self.merk} {self.model} ({self.tahun})"

# Service records for the cars
class Service(models.Model):
    mobil = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='services')  # Linked to Car
    tanggal = models.DateField()
    deskripsi = models.TextField()
    biaya = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Service {self.mobil.merk} - {self.mobil.model} on {self.tanggal}"

    def car_display(self):
        return self.car.merk 
    car_display.short_description = 'Car Merk'