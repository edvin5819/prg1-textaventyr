namn = input ("hej spelare välj ett coach namn.")
tid = float(0)
snabhet = float(1.0)
print (f"nu ska du {namn} få coatcha Ted innan hans 100meter race.")
frukost = input ("tycker du ted ska ätta en (omellet) eller (gröt) till frukost?")
if frukost.lower() == "gröt":
    print ("bra val")
    snabhet = snabhet * 1.1
elif frukost.lower() == "omellet":
    print ("bra val")
else:
    frukost = input ("du har bara egg och havre hemma du måste välja (gröt) eller (omellet) vad väljer du?")
    if frukost.lower() == "gröt":
        print ("bra val")
        snabhet = snabhet * 1.1
    elif frukost.lower() == "omellet":
        print ("bra val")
    else:
        print ("du dog")
        exit()
transport = input ("hur ska du ta dig till tävlingen ska du (cykla) eller (fråga om skjuts)?")
if transport.lower() == "fråga om skjuts":
    upvärmnining = "inte alls"
    input ("du behövde vänta på mamma så du kom sent och har ingen tid att värma upp")
elif transport.lower() == "cykla":
    upvärmnining = input ("du kom i bra tid så då kan du välja om du ska värma upp (en timme), (tjugo minuter) eller (inte alls). hur länge värmer du upp?")
else:
    transport = input ("du måste (cykla) eller (fråga om skjuts) annars kommer du inte till tävlingen vad väljer du?")
    if transport.lower() == "fråga om skjuts":
        print ("du blir sen får ingen upvärmning")
        upvärmnining = "inte alls"
    elif transport.lower() == "cykla":
        print ("du kommer i tid")
        upvärmnining = input ("du kom i bra tid så då kan du välja om du ska vära upp (en timme) (tjugo minuter) eller (inte alls). hur länge värmer du upp?")
    else:
        print ("du missade tävlingen")
        exit()
if upvärmnining.lower() == "en timme":
    print ("det var länge, nu blev ted tröt innen sitt lopp")
    snabhet = snabhet * 0.9
elif upvärmnining.lower() == "tjugo minuter":
    print ("bra val")
    snabhet = snabhet * 1.05
elif upvärmnining.lower() == "ingen alls":
    print("du sparar altså all hans energi")
    snabhet = snabhet * 0,9
energi = input ("du måste få i dig energi innan tävlingen så du måste välja om ted ska ta en (energibar), en (energidricka) eller en (munk) vad ska han ha?")
if energi.lower() == "energibar":
    print ("bra val")
    snabhet = snabhet * 1.05
elif energi.lower() == "energidricka":
    print ("superbra val")
    snabhet = snabhet * 1.1
elif energi.lower() == "munk":
    print ("oj det var ett dåligt val")
    snabhet = snabhet * 0.95
else: 
    energi = input ("du måste välja något att äta annar orkar du inte. vill du ha (energidricka) eller (energibar)?")
    if energi.lower() == "energibar":
        print ("bra val")
        snabhet = snabhet * 1.05
    elif energi.lower() == "energidricka":
        print ("bra val")
        snabhet = snabhet * 1.1
    else:
        exit("du hade ingen energi och orkade inte springa")
if frukost.lower() == "omellet":
    print ("ted blev jätte bajsnödig just innan reacet på grund av omelleten till frukost så han behövde gå och bajsa och missade racet") 
    exit()
else:
    tid = 13 / snabhet * 100
    tid = int(tid) 
    print (f" du sprang på {tid / 100}sekunder") 
if tid/100 < 10.5:
        print (f"bra coachat {namn}. ted van!!!!")
elif tid/100 < 11.0:
        print (f"bra coachat {namn}. ted kom på andra plats!!")
elif tid/100 < 11.5:
        print (f"bra coachat {namn}. ted kom trea!")
elif tid/100 < 12.0:
        print ("helt okej ted kom på fjärde plats!")
elif tid/100 < 12.5:
        print ("ganska dåligt ted kom fema och näst sist")
else:
     print ("ted kom tyvär sist och du var en väldigt dålig coach")
   