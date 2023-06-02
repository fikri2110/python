
def Header():
    '''program membuat kalkulasi kwh listrik'''
    print(f"{'PROGRAM APLIKASI MENGHITUNG SISA KWH':^40}")
    
def perhitungan():
    nilai_terakhir = int(input(f" MASUKAN NILAI KWH TERAKHIR = "))
    nilai_awal = int(input(f" MASUKAN NILAI KWH AWAL = ")) 
    return nilai_terakhir,nilai_awal
    
def kalkulasi(nilai_terakhir,nilai_awal):
    return nilai_terakhir - nilai_awal


while True :
    Header()
    AWAL,AKHIR = perhitungan()
    hasil = kalkulasi(AWAL,AKHIR)
    
    print(f"nilai sisa kwh = {hasil}")
    itscontinue = input("Apakah Lanjut y/n ?")
    if  itscontinue == "n":
        break
print("Program Sudah Selesai..")