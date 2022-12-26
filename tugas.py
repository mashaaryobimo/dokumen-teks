print('\nProgram Data Mahasiswa')
print('Nama : Angga Prasetyo')
print('NIM : L200220154')
print('Prodi : Tehnik Informatika')

list_NIM = []
list_Nama = []
list_Prodi = []
list_Nilai = []

class DataMahasiswa:
    
    def _inif_(self, NIM, Nama, Prodi, Nilai):
        self.NIM = NIM
        list_NIM.append(self.NIM)
        self.Nama = Nama
        list_NIM.append(self.Nama)
        self.Prodi = Prodi
        list_Prodi.append(self.Prodi)
        self.Nilai = Nilai
        list_Nilai.append(self.Nilai)
    
    def tampilData (self):
        n = 0
        print('\nJumlah Mahasiswa yang sudah TerInput :',x)
        for i in range (x):
            n += 1
            if len(list_Nilai[i]) >= 50 :
                print('\n---------Mahasiswa ke-',n,'----------------')
                print('NIM Mahasiswa :',list_NIM[i])
                print('Nama Mahasiswa :',list_Nama[i])
                print('Nilai Mahasiswa :',list_Nilai[i])
                print('---------------------------------------------')
            else :
                i += 1
                print('Catatan : Apabila Mahasiswa yang tidak ditampilkan karna Nilai Kurang dari rata-rata')


stop = False
x = 0

while (not stop) :
    inputNIM = input('Masukkan NIM :')
    inputNama = input('Masukkan Nama :')
    inputProdi = input('Masukkan Prodi :')
    inputNilai =int(input('Masukkan Nilai :'))
    Mahasiswa = DataMahasiswa()
    #9print(Mahasiswa.tampilData())
    
    x += 1
    ulang = input('Apakah anda ingin input ulang(y/t) ? :')
    if ulang == 't' :      
        break
        
Mahasiswa.tampilData()
    
                
            
        
    