import datetime

def hello():
    print("                               — Welcome to İSTİNYE Bank —")
    print(("                                       İSTANBUL"))
    import datetime
    tarihsaat = datetime.datetime.now().strftime("                                   %d-%m-%Y %H:%M:%S");
    print(tarihsaat)
hello()

login=False
kullanici_adlari = ["Ahmed","Zeynep","Alberto"]
sifreler = [1234, 4321, 4422]
hesaplar = {"Ahmed": 1234, "Zeynep": 4321, "Alberto": 4422}
bakiyeler = {"Ahmed":100, "Zeynep":200, "Alberto":300}
islemler = {"Ahmed": [], "Zeynep": [], "Alberto": []}
while True:
    if login == False:
        islem = input("1.Login \n2.Exit \n")
    if islem == "2":
        print("Logged Out")
        break
    elif islem == "1":
        secenek = input("What do you want to login us: \n1.Admin \n2.User \n3.Go Back \n")
        if secenek == "3":
            islem = input("1.Login \n2.Exit \n")
        if secenek == "1":
            print("")
        elif secenek == "2":
            isim = input("Username:")
            if isim in kullanici_adlari:
                parola = input("Password:")
                if isim in kullanici_adlari and int(parola) == hesaplar[isim]:
                    print("{} Welcome to Sehir Bank \Please enter the number of the service: \n".format(isim))
                    while True:
                        secenek= input("1.Withdraw Money \n2.Deposit Money \n3.Transfer Money \n4.My Account Information \n5.Logout \n")
                        login = True
                        if secenek == "1":
                            miktar = int(input("Please enter the amount you want to withdraw:"))
                            if bakiyeler[isim] < miktar:
                                print("You don’t have miktar TL in your account \nGoing back to main menu..")
                            if bakiyeler[isim] >= miktar:
                                tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S");
                                print(tarihsaat)
                                print("{} TL withdrawn from your account \nGoing back to main menu...".format(miktar))
                                bakiyeler[isim] -= miktar
                                islemler[isim].append("Hesabınızdan " + str(miktar) + " tl para çekildi tarih: " + str(tarihsaat))
                                print("Hesabınızdan " + str(miktar) + " tl para çekildi tarih: " + str(tarihsaat))
                        elif secenek == "2":
                            miktar = int(input("Please enter the amount you want to drop:"))
                            import datetime
                            tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S");
                            print(tarihsaat)
                            print("{} TL added to your account \nGoing back to main menu...".format(miktar))
                            bakiyeler[isim] =+ miktar
                            islemler[isim].append("Hesabınıza " + str(miktar) + " tl para eklendi tarih: " +str(tarihsaat))
                            print("Hesabınıza " + str(miktar) + " tl para eklendi tarih: " +str(tarihsaat))
                        elif secenek == "3":
                            kisi = input("Warning: If you want  to abort the transfer please enter abort \nPlease enter the name of the user you want transfer money to:")
                            if kisi == "abort":
                                print("Going back to main menu")
                            elif kisi in kullanici_adlari and kisi != isim:
                                miktar = int(input("Please enter the amount you want to transfer:"))
                                if (bakiyeler[isim] < miktar):
                                    print("Sorry! You don’t have enough money to complete this transaction")
                                    q1 = input("1. Go back to main menu \n2. Transfer again")
                                elif (bakiyeler[isim] >= miktar):
                                    tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                    bakiyeler[isim] -= miktar
                                    bakiyeler[kisi] += miktar
                                    islemler[isim].append(str(miktar) + " tl " + kisi + " isimli kullanıcıya gönderildi tarih: " + str(tarihsaat))
                                    islemler[kisi].append(str(miktar) + " tl hesabınıza " + isim + " tarafından gönderildi tarih: " + str(tarihsaat))
                                    print(str(miktar) + " tl " + kisi + " isimli kullanıcıya gönderildi tarih: " + str(tarihsaat))
                                    print("Money transfer successful")
                            else:
                                print(
                                    "Transferring to user with the name {} is not possible! User does not exist!".format(kisi))
                        elif secenek == "4":
                            print("Your Name: {} \nYour Password: {} \nYour Balance Amount (TL): {} \n     -------------".format(isim, parola, bakiyeler[isim]))
                            print("User Activities Report:\n     -------------")
                            print(islemler[isim])
                        elif secenek == "5":
                            break
                            islem = input("1.Login \n2.Exit")
        else:
            print("Please enter a number that is a valid input")