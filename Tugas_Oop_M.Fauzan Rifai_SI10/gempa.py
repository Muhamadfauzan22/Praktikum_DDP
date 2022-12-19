class Gempa:
    # member 1 variabel

    lokasi = ""
    skala = 0
    
    # member 2 konstrruktur
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
        
        # member 3 method
    def dampak(self):
        if(self.skala < 2):
            ket ="tidak terasa"
        elif(self.skala >=2 and self.skala <4):
            ket = "Bangunan retak - retak"
        elif(self.skala >=4 and self.skala <6):
            ket = "Bangunan pada roboh"
        else:
            ket = "Bangunan roboh dan berpotensi tsunami"

        print(
            '\nlokasi gempa\t:',self.lokasi,
            '\nskala\t\t:',self.skala,'richter'
            '\ndampak\t\t:',ket,
            '\n===============================')