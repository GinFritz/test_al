# Python test code

import scraperwiki
import BeautifulSoup
import urllib2
import string


lastrec = 25000
i = 1

while i < lastrec:
    try:
        html = scraperwiki.scrape('http://www.ordineavvocati.roma.it/AlboElenchi/AlboAvvocati/SchedaIscritto.asp?ID=' + str(i))
        soup = BeautifulSoup.BeautifulSoup(html)
        id_avv=i
        print id_avv
        i=i+1
        j=0
        for dato_avv in soup.findAll('td'):
            x = str(dato_avv)
            j=j+1
            if j==17:
                foro = str(dato_avv.string)
                print foro
            elif j==29:
                codfisc = str(dato_avv.string)
                print codfisc

        k=0
        for dato_avv in soup.findAll('strong'):
            x = str(dato_avv)
            k=k+1
            if k==2:
                cognomenome = str(dato_avv.string)
                print cognomenome

        h=0
        for dato_avv in soup.findAll('a'):
            x = str(dato_avv)
            h=h+1
            if h==112:
                email = str(dato_avv.string)
                print email

        w=0
        for dato_avv in soup.findAll('p'):
            x = str(dato_avv)
            w=w+1
            if w==3:
                indiriz = str(dato_avv.string)
                print indiriz
            elif w==4:
                tel1 = str(dato_avv.string)
                print tel1


        scraperwiki.sqlite.save(unique_keys=["Codice fiscale"], data = {"Codice fiscale":codfisc, "Email":email, "CognomeNome":cognomenome, "Indirizzo":indiriz, "Telefono":tel1, "Progressivo":id_avv, "Foro":foro})

    except:
        i=i+1
        continue
