# Import
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from os import path
import time
import csv
import subprocess

# Setup
with open("data_fyzicka_osoba.csv", "r", encoding="utf-8") as csv_zdroj:
    csv_reader = csv.reader(csv_zdroj, delimiter=";")

    # Vyplnění formuláře
    next(csv_reader, None)

    for data in csv_reader:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        web = webdriver.Chrome(
            executable_path="C:/Autofill/chromedriver.exe", options=chrome_options
        )

        web.execute_cdp_cmd(
            "Network.setUserAgentOverride",
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36"
            },
        )

        web.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        web.get("https://zadost.pgrlf.cz/Form/ZpracovatelDreva")

        time.sleep(1)

        try:
            FyzickaOsoba = web.find_element_by_id("rbFyzickaOsoba")
            if FyzickaOsoba.is_selected() == False:
                FyzickaOsoba.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Fyzická osoba nebyla zvolena")

        try:
            TitulPredJmenem = web.find_element_by_name("FyzickaOsoba.TitulPredJmenem")
            TitulPredJmenem.send_keys(data[0])

        except:
            print("Titul před jménem nebyl vyplněn")

        try:
            Jmeno = web.find_element_by_name("FyzickaOsoba.Jmeno")
            Jmeno.send_keys(data[1])

        except:
            print("Jméno nebylo vyplněno")

        try:
            Prijmeni = web.find_element_by_name("FyzickaOsoba.Prijmeni")
            Prijmeni.send_keys(data[2])

        except:
            print("Příjmení nebylo vyplněno")

        try:
            TitulZaJmenem = web.find_element_by_name("FyzickaOsoba.TitulZaJmenem")
            TitulZaJmenem.send_keys(data[3])

        except:
            print("Titul za jménem nebyl vyplněn")

        try:
            if data[4] == "Ne":
                JePlatceDPH = web.find_element_by_name("FyzickaOsoba.JePlatceDPH")
                JePlatceDPH.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Plátce DPH nebyl zvolen")

        try:
            IC = web.find_element_by_name("FyzickaOsoba.IC")
            IC.send_keys(data[5])

        except:
            print("IČ nebylo vyplněno")

        try:
            if data[4] == "Ano":
                DIC = web.find_element_by_name("FyzickaOsoba.DIC")
                DIC.send_keys(data[6])

        except:
            print("DIČ nebylo vyplněno")

        try:
            RodneCislo = web.find_element_by_name("FyzickaOsoba.RodneCislo")
            RodneCislo.send_keys(data[7])

        except:
            print("Rodné číslo nebylo vyplněno")

        try:
            DatumNarozeni = web.find_element_by_name("FyzickaOsoba.DatumNarozeni")
            DatumNarozeni.send_keys(data[8])

        except:
            print("Datum narození nebyl vyplněn")

        try:
            TrvalyPobyt_Ulice = web.find_element_by_name(
                "FyzickaOsoba.TrvalyPobyt.Ulice"
            )
            TrvalyPobyt_Ulice.send_keys(data[9])

        except:
            print("Trvalý pobyt - ulice nebyla vyplněna")

        try:
            TrvalyPobyt_CisloPopisne = web.find_element_by_name(
                "FyzickaOsoba.TrvalyPobyt.CisloPopisne"
            )
            TrvalyPobyt_CisloPopisne.send_keys(data[10])

        except:
            print("Trvalý pobyt - číslo popisné nebylo vyplněno")

        try:
            TrvalyPobyt_CisloOrientacni = web.find_element_by_name(
                "FyzickaOsoba.TrvalyPobyt.CisloOrientacni"
            )
            TrvalyPobyt_CisloOrientacni.send_keys(data[11])

        except:
            print("Trvalý pobyt - číslo orientační nebylo vyplněno")

        try:
            TrvalyPobyt_Obec = web.find_element_by_name("FyzickaOsoba.TrvalyPobyt.Obec")
            TrvalyPobyt_Obec.send_keys(data[12])

        except:
            print("Trvalý pobyt - obec nebyla vyplněna")

        try:
            TrvalyPobyt_PSC = web.find_element_by_name("FyzickaOsoba.TrvalyPobyt.PSC")
            TrvalyPobyt_PSC.send_keys(data[13])

        except:
            print("Tryvalý pobyt - PSČ nebylo vyplněno")

        try:
            TrvalyPobyt_Kraj = Select(
                web.find_element_by_name("FyzickaOsoba.TrvalyPobyt.Kraj")
            )
            TrvalyPobyt_Kraj.select_by_visible_text(data[14])

        except:
            print("Trvalý pobyt - kraj nebyl vyplněn")

        try:
            if data[15] == "Ano":
                JeMistoPodnikaniStejne = web.find_element_by_name(
                    "FyzickaOsoba.JeMistoPodnikaniStejne"
                )

                JeMistoPodnikaniStejne.send_keys(webdriver.common.keys.Keys.SPACE)

            else:
                try:
                    MistoPodnikani_Ulice = web.find_element_by_name(
                        "FyzickaOsoba.MistoPodnikani.Ulice"
                    )
                    MistoPodnikani_Ulice.send_keys(data[16])

                except:
                    print("Místo podníkání - ulice nebyla vyplněna")

                try:
                    MistoPodnikani_CisloPopisne = web.find_element_by_name(
                        "FyzickaOsoba.MistoPodnikani.CisloPopisne"
                    )
                    MistoPodnikani_CisloPopisne.send_keys(data[17])

                except:
                    print("Místo podnikání - číslo popisné nebylo vyplněno")

                try:
                    MistoPodnikani_CisloOrientacni = web.find_element_by_name(
                        "FyzickaOsoba.MistoPodnikani.CisloOrientacni"
                    )
                    MistoPodnikani_CisloOrientacni.send_keys(data[18])

                except:
                    print("Místo podnikání - číslo orientační nebylo vyplněno")

                try:
                    MistoPodnikani_Obec = web.find_element_by_name(
                        "FyzickaOsoba.MistoPodnikani.Obec"
                    )
                    MistoPodnikani_Obec.send_keys(data[19])

                except:
                    print("Místo podnikání - obec nebyla vyplněna")

                try:
                    MistoPodnikani_PSC = web.find_element_by_name(
                        "FyzickaOsoba.MistoPodnikani.PSC"
                    )
                    MistoPodnikani_PSC.send_keys(data[20])

                except:
                    print("Místo podnikání - PSČ nebylo vyplněno")

                try:
                    MistoPodnikani_Kraj = Select(
                        web.find_element_by_name("FyzickaOsoba.MistoPodnikani.Kraj")
                    )
                    MistoPodnikani_Kraj.select_by_visible_text(data[21])

                except:
                    print("Místo podníkání - kraj nebyl vyplněn")

        except:
            print("Místo podníkání je stejné nebylo zvoleno")

        try:
            Kontakt_Telefon1 = web.find_element_by_name("Kontakt.Telefon1")
            Kontakt_Telefon1.send_keys(data[22])

        except:
            print("Kontakt - hlavní telefon nebyl vyplněn")

        try:
            Kontakt_Telefon2 = web.find_element_by_name("Kontakt.Telefon2")
            Kontakt_Telefon2.send_keys(data[23])

        except:
            print("Kontakt - vedlejší telefon nebyl vyplněn")

        try:
            Kontakt_Email = web.find_element_by_name("Kontakt.Email")
            Kontakt_Email.send_keys(data[24])

        except:
            print("Kontakt - email nebyl vyplněn")

        try:
            BankovniSpojeni_CisloUctu = web.find_element_by_name(
                "BankovniSpojeni.CisloUctu"
            )
            BankovniSpojeni_CisloUctu.send_keys(data[25])

        except:
            print("Bankovní spojení - číslo účtu nebylo vyplněno")

        try:
            BankovniSpojeni_KodBanky = web.find_element_by_name(
                "BankovniSpojeni.KodBanky"
            )
            BankovniSpojeni_KodBanky.send_keys(data[26])

        except:
            print("Bankovní spojení - kód banky nebyl vyplněn")

        try:
            ObchodniRejstrikFyzicka_ORZapis = web.find_element_by_name(
                "ObchodniRejstrikFyzicka.ORZapis"
            )
            ObchodniRejstrikFyzicka_ORZapis.send_keys(data[27])

        except:
            print("Obchodní rejstřík - spisová značka nebyla vyplněna")

        try:
            ObchodniRejstrikFyzicka_ORVydal = web.find_element_by_name(
                "ObchodniRejstrikFyzicka.ORVydal"
            )
            ObchodniRejstrikFyzicka_ORVydal.send_keys(data[28])

        except:
            print("Obchodní rejstřík - příslušný krajský soud nebyl vyplněn")

        try:
            ObchodniRejstrikFyzicka_ORDatum = web.find_element_by_name(
                "ObchodniRejstrikFyzicka.ORDatum"
            )
            ObchodniRejstrikFyzicka_ORDatum.send_keys(data[29])

        except:
            print("Obchodní rejstřík - datum vydání nebyl vyplněn")

        try:
            if data[30] == "Ano":
                PlanovaneUkonceni_UkonceniCinnosti = web.find_element_by_name(
                    "PlanovaneUkonceni.UkonceniCinnosti"
                )
                PlanovaneUkonceni_UkonceniCinnosti.send_keys(
                    webdriver.common.keys.Keys.SPACE
                )

                try:
                    PlanovaneUkonceni_UkonceniCinnostiDatum = web.find_element_by_name(
                        "PlanovaneUkonceni.UkonceniCinnostiDatum"
                    )
                    PlanovaneUkonceni_UkonceniCinnostiDatum.send_keys(data[31])

                except:
                    print("Plánované ukončení - datum ukončení činnosti nebyl vyplněn")

        except:
            print("Ukončení činnosti nebylo zvoleno")

        try:
            if data[32] == "Ano":
                PlanovanyProdej_ProdejPodniku = web.find_element_by_name(
                    "PlanovanyProdej.ProdejPodniku"
                )
                PlanovanyProdej_ProdejPodniku.send_keys(
                    webdriver.common.keys.Keys.SPACE
                )

                try:
                    PlanovanyProdej_ProdejPodnikuDatum = web.find_element_by_name(
                        "PlanovanyProdej.ProdejPodnikuDatum"
                    )
                    PlanovanyProdej_ProdejPodnikuDatum.send_keys(data[33])

                except:
                    print("Plánované ukončení - datum prodeje podniku nebyl vyplněn")

        except:
            print("Prodej podniku nebyl zvolen")

        # Podpis - čestné prohlášení
        try:
            Podpis = web.find_element_by_name("CestneProhlaseni")
            Podpis.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Podpis nebyl zvolen")

        # Podpis - Deminimis čestné prohlášení
        try:
            Podpis_DM = web.find_element_by_name("DeMinimis.DMCestneProhlaseni")
            Podpis_DM.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Podpis - de minimis nebyl zvolen")

        try:
            UverInvesticni_VyseUveru = web.find_element_by_name(
                "UverInvesticni.VyseUveru"
            )
            UverInvesticni_VyseUveru.send_keys(data[34])

        except:
            print("Úvěr investiční - výše úvěru nebyla vyplněna")

        try:
            UverInvesticni_DobaSplatnosti = web.find_element_by_name(
                "UverInvesticni.DobaSplatnosti"
            )
            UverInvesticni_DobaSplatnosti.send_keys(data[35])

        except:
            print("Úvěr investiční - doba splatnosti nebyla vyplněna")

        try:
            UverInvesticni_OdkladSplatky = web.find_element_by_name(
                "UverInvesticni.OdkladSplatky"
            )
            UverInvesticni_OdkladSplatky.send_keys(data[36])

        except:
            print("Úvěr investiční - odklad splátky nebyl vyplněn")

        try:
            UverInvesticni_ZduvodneniOdkladuInvesticni = web.find_element_by_name(
                "UverInvesticni.ZduvodneniOdkladuInvesticni"
            )
            UverInvesticni_ZduvodneniOdkladuInvesticni.send_keys(data[37])

        except:
            print("Úvěr investiční - zdůvodnění odkladu splátky nebylo vyplněno")

        try:
            if data[38] == "Ne":
                jeSnizeni = web.find_element_by_name("jeSnizeni")
                jeSnizeni.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Snížení jistiny nebylo zvoleno")

        try:
            if data[39] == "Ano":
                jeZacinajici = web.find_element_by_name("jeZacinajici")
                jeZacinajici.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Začínající podnikatel nebyl zvolen")

        # TEST PROMĚNNÝCH
        #print(" ")
        #print("----------------------------------------")
        #print("TEST PROMĚNNÝCH")
        #print("----------------------------------------")
        #print(" ")
        #print("Titul před jménem: ", data[0])
        #print("Jméno: ", data[1])
        #print("Příjmení: ", data[2])
        #print("Titul za jménem: ", data[3])
        #print("Plátce DPH: ", data[4])
        #print("IČ: ", data[5])
        #print("DIČ: ", data[6])
        #print("Rodné číslo: ", data[7])
        #print("Datum narození: ", data[8])
        #print("Trvaly pobyt - ulice: ", data[9])
        #print("Trvaly pobyt - ČP: ", data[10])
        #print("Trvaly pobyt - ČO: ", data[11])
        #print("Trvaly pobyt - obec: ", data[12])
        #print("Trvaly pobyt - PSČ: ", data[13])
        #print("Trvaly pobyt - kraj: ", data[14])
        #print("JeMistoPodnikaniStejne: ", data[15])
        #print("MistoPodnikani.Ulice: ", data[16])
        #print("MistoPodnikani.CisloPopisne: ", data[17])
        #print("MistoPodnikani.CisloOrientacni: ", data[18])
        #print("MistoPodnikani.Obec: ", data[19])
        #print("MistoPodnikani.PSC: ", data[20])
        #print("MistoPodnikani.Kraj: ", data[21])
        #print("Kontakt.Telefon1: ", data[22])
        #print("Kontakt.Telefon2: ", data[23])
        #print("Kontakt.Email: ", data[24])
        #print("BankovniSpojeni.CisloUctu: ", data[25])
        #print("BankovniSpojeni.KodBanky: ", data[26])
        #print("ObchodniRejstrikFyzicka.ORZapis: ", data[27])
        #print("ObchodniRejstrikFyzicka.ORVydal: ", data[28])
        #print("ObchodniRejstrikFyzicka.ORDatum: ", data[29])
        #print("PlanovaneUkonceni.UkonceniCinnosti: ", data[30])
        #print("PlanovaneUkonceni.UkonceniCinnostiDatum: ", data[31])
        #print("PlanovanyProdej.ProdejPodniku: ", data[32])
        #print("PlanovanyProdej.ProdejPodnikuDatum: ", data[33])
        #print("UverInvesticni.VyseUveru: ", data[34])
        #print("UverInvesticni.DobaSplatnosti: ", data[35])
        #print("UverInvesticni.OdkladSplatky: ", data[36])
        #print("UverInvesticni.ZduvodneniOdkladuInvesticni: ", data[37])
        #print("jeSnizeni: ", data[38])
        #print("jeZacinajici: ", data[39])

        time.sleep(3600)