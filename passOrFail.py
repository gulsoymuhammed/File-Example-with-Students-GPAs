def notHesapla(satir):
    #remove the end line character
    satir=satir[:-1]
    liste=satir.split(",")
    #separate them with their qualifications respectively
    isim=liste[0]
    vize1=int(liste[1])
    vize2=int(liste[2])
    vize3=int(liste[3])
    #GPA calculation
    genelNot=(3/10)*vize1+(3/10)*vize2+(4/10)*vize3

    if(genelNot>90):
        sinavNotu="AA"
    elif(85<=genelNot):
        sinavNotu="BA"
    elif(80<=genelNot):
        sinavNotu="BB"
    elif(70<=genelNot):
        sinavNotu="CB"
    elif(65<=genelNot):
        sinavNotu="CC"
    elif(60<=genelNot):
        sinavNotu="DC"
    elif(55<=genelNot):
        sinavNotu="DD"
    elif(50<=genelNot):
        sinavNotu="FD"
    else:
        sinavNotu="FF"
    return isim+"------------------------------------>"+sinavNotu+"\n"



with open("dosya.txt","r",encoding="utf-8") as file:
  
    sonHalListe=list()
    for i in file:
        #it sends every line one by one and append the list that named of sonHalListe 
        sonHalListe.append(notHesapla(i))

#writing sonHalListe in notlar.txt   
with open("notlar.txt","w",encoding="utf-8") as file:
    file.writelines(sonHalListe)



def gecmeKalma(harfnotu):
    if (harfNotu=="FF" or harfNotu =="FD"):
        return "kaldiniz"
    
#reading notlar.txt and refining string
with open("notlar.txt","r",encoding="utf-8") as file:
    gecenlerListesi=list()
    kalanlarListesi=list()
    for satir in file:
        satir=satir[:-1]
        liste=satir.split("-")
        isim=liste[0]
        harfNotu=liste[-1]
        harfNotu=harfNotu[1:]
        #if GPA is low,append student in kalanlar Listesi with its GPA.Else, append it in gecenlerListesi which is formed for student who pass the lesson
        if(gecmeKalma(harfNotu)=="kaldiniz"):
            kalanlarListesi.append(isim+" "+harfNotu+"\n")
        else:
            gecenlerListesi.append(isim+" "+harfNotu+"\n")

#writing students who pass the  lesson on gecenler.txt
with open("gecenler.txt","w",encoding="utf-8") as file:
    file.write("GECENLER\n")
    file.writelines(gecenlerListesi)   

#writing students who fail the  lesson on kalanlar.txt   
with open("kalanlar.txt","w",encoding="utf-8") as file:
    file.write("KALANLAR\n")
    file.writelines(kalanlarListesi)
