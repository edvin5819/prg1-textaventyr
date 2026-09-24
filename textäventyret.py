namn = input ("hej spelare välj ett splarnamn.")
tid = float(0)
snabhet = float(1.0)
print (f"nu ska du {namn} få coatcha Ted innan hans 100meter race.")
frukost = input ("tycker du ted ska ätta en omellet eller gröt till frukost?")
if frukost == "gröt":
    print ("bra val")
    snabhet = snabhet * 1.2
elif frukost == "omellet":
    print ("bra val")
else:
    frukost = input ("du har bara egg och havre hemma du måste välja gröt eller omellet vad väljer du?")
    if frukost.lower() == "gröt":
        print ("bra val")
        snabhet = snabhet * 1.2
    elif frukost.lower() == "omellet":
        print ("bra val")
    else:
        print ("du dog")
        exit()
transport = input ("hur ska du ta dig till tävlingen ska du cykla eller fråga om skjuts?")
if transport.lower() == "fråga om skjuts":
    input ("du behövde vänta på mamma så du kom sent och har ingen tid att värma upp")
elif transport.lower() == "cykla":
    upvärmnining = input ("du kom i bra tid så då kan du välja om du ska vära upp en timme tjugo minuter eller inte alls. hur länge värmer du upp?")
else:
    transport = input ("du måste cykla eller fråga om skjuts annars kommer du inte till tävlingen vad väljer du?")
    if transport.lower() == "fråga om skjuts":
        print ("du blir sen får ingen upvärmning")
    elif transport.lower() == "cykla":
        print ("du kommer i tid")
        upvärmnining = input ("du kom i bra tid så då kan du välja om du ska vära upp en timme tjugo minuter eller inte alls. hur länge värmer du upp?")
    else:
        print ("du missade tävlingen")
        exit()
if upvärmnining.lower() == "en timme":
    print ("det var länge, nu blev ted tröt innen sitt lopp")
    snabhet = snabhet * 0.9
elif upvärmnining.lower() == "tjugo minuter":
    print ("bra val")
    snabhet = snabhet * 1.1
elif upvärmnining.lower() == "ingen alls":
    print("du sparar altså all hans energi")
    snabhet = snabhet * 0,9
energi = input ("du måste få i dig energi innan tävlingen så du måste välja om ted ska ta en energibar eller en energidricka vad ska han ha?")
if energi.lower() == "energibar":
    print ("bra val")
    snabhet = snabhet * 1.1
if energi.lower() == "energidricka":
    print ("superbra val")
    snabhet = snabhet * 1.2
else:
    energi = input ("du måste välja något att äta annar orkar du inte. vill du ha energidricka eller energibar?")
    if energi.lower() == "energibar":
        print ("bra val")
        snabhet = snabhet * 1.1
    if energi.lower() == "energidricka":
        print ("bra val")
        snabhet = snabhet * 1.2
    else:
        exit("du hade ingen energi och orkade inte springa")
if frukost.lower == "omellet":
    print ("ted blev jätte bajsnödig just innan reacet på grund av omelleten till frukost så han behövde gå och bajsa och missade racet") 
    exit()
else:
    print (f"bra jobbat du sprang på {11 / snabhet}sekunder")