import hashlib


def irudiKodetuta():
    #Argazkien arteko ezberdintasun bakarra bere zenbakia da, beraz 2 string sortu ditut constante moduan erabili ahal izateko
    imagen="imagen"
    jpg=".jpg"

    #Argazkien path absolutua sartu dut, programak jakin dezala non bilatu argazkiak
    path="/home/ander/Escritorio/UNI/3.maila/Segurtasuna/Laborategiak/2 Laborategia - Zifraketa-20211008/irudia/"

    i=1
    #Hash kode ona gorde gero argakien hash kodeekin konparatzeko eta ona aurkitzeko
    kodeona = "e5ed313192776744b9b93b1320b5e268"

    #while bat argazki guztiak banan banan begiratzen joateko
    while i<47:
        #27. argazkia ez denez existitzen, salbuespen moduan if bat argazki hori saltatzeko
        if i == 27:
            i = i + 1
        j=str(i)
        arIzena= path+imagen+j+jpg

        #uneko argazkia zabaltzen eta irakurtzen da.
        with open(arIzena, 'rb') as f:

            bytes=f.read() #artxiboa byte-ak bezala irakurri

            #informazioa bueltatzen da string bezala
            hash=hashlib.md5(bytes).hexdigest()

            #aurkitzen badu, aurkitu duela eta zein den esan
            if hash==kodeona:
                print("\nArgazkia aurkitu da eta hau da: ")
                print(arIzena + "\neta bere hash kodea hau da: "+hash)
            i=i+1







irudiKodetuta()