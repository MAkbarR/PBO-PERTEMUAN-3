class VolumeBalok :
    Panjang =  None
    Lebar = None
    Tinggi = None

VB = VolumeBalok()
VolumeBalok.Panjang = 4
VolumeBalok.Lebar = 8
VolumeBalok.Tinggi = 16

Hasil = VolumeBalok.Panjang*VolumeBalok.Lebar*VolumeBalok.Tinggi

print("Panjang Balok :", VolumeBalok.Panjang)
print("Lebar Balok :", VolumeBalok.Lebar)
print("Tinggi Balok :", VolumeBalok.Tinggi)
print("Hasil Volume Balok:", Hasil)