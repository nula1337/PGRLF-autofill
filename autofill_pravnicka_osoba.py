# Import
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from os import path
import time
import csv
import subprocess

# Setup
with open("data_pravnicka_osoba.csv", "r", encoding="utf-8") as csv_zdroj:
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

        web.get("https://zadost.pgrlf.cz/Form/InvesticniUverZemedelecTiket")

        time.sleep(1)

        try:
            PravnickaOsoba = web.find_element_by_id("rbPravnickaOsoba")
            if PravnickaOsoba.is_selected() == False:
                PravnickaOsoba.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Pravnická osoba nebyla zvolena")

        try:
            ObchodniJmeno = web.find_element_by_name("PravnickaOsoba.ObchodniJmeno")
            ObchodniJmeno.send_keys(data[0])

        except:
            print("Obchodní jméno nebylo vyplněno")

        try:
            TypPO = web.find_element_by_name("PravnickaOsoba.TypPO")
            TypPO.send_keys(data[1])

        except:
            print("Typ společnosti nebyl vyplněn")

        try:
            if data[2] == "Ne":
                JePlatceDPH = web.find_element_by_name("PravnickaOsoba.JePlatceDPH")
                JePlatceDPH.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Plátce DPH nebyl zvolen")

        try:
            IC = web.find_element_by_name("PravnickaOsoba.IC")
            IC.send_keys(data[3])

        except:
            print("IČ nebylo vyplněno")

        try:
            DIC = web.find_element_by_name("PravnickaOsoba.DIC")
            DIC.send_keys(data[4])

        except:
            print("DIČ nebylo vyplněno")

        try:
            SidloSpolecnosti_Ulice = web.find_element_by_name(
                "PravnickaOsoba.SidloSpolecnosti.Ulice"
            )
            SidloSpolecnosti_Ulice.send_keys(data[5])

        except:
            print("Sídlo společnosti - ulice nebyla vyplněna")

        try:
            SidloSpolecnosti_CisloPopisne = web.find_element_by_name(
                "PravnickaOsoba.SidloSpolecnosti.CisloPopisne"
            )
            SidloSpolecnosti_CisloPopisne.send_keys(data[6])

        except:
            print("Sídlo společnosti - číslo popisné nebylo vyplněno")

        try:
            SidloSpolecnosti_CisloOrientacni = web.find_element_by_name(
                "PravnickaOsoba.SidloSpolecnosti.CisloOrientacni"
            )
            SidloSpolecnosti_CisloOrientacni.send_keys(data[7])

        except:
            print("Sídlo společnosti - číslo orientační nebylo vyplněno")

        try:
            SidloSpolecnosti_Obec = web.find_element_by_name(
                "PravnickaOsoba.SidloSpolecnosti.Obec"
            )
            SidloSpolecnosti_Obec.send_keys(data[8])

        except:
            print("Sídlo společnosti - obec nebyla vyplněna")

        try:
            SidloSpolecnosti_PSC = web.find_element_by_name(
                "PravnickaOsoba.SidloSpolecnosti.PSC"
            )
            SidloSpolecnosti_PSC.send_keys(data[9])

        except:
            print("Sídlo společnosti - PSČ nebylo vyplněno")

        try:
            SidloSpolecnosti_Kraj = Select(
                web.find_element_by_name("PravnickaOsoba.SidloSpolecnosti.Kraj")
            )
            SidloSpolecnosti_Kraj.select_by_visible_text(data[10])

        except:
            print("Sídlo společnosti - kraj nebyl nebyl vyplněn")

        try:
            if data[11] == "Ano":
                JeMistoPodnikaniStejne = web.find_element_by_name(
                    "PravnickaOsoba.JeMistoPodnikaniStejne"
                )

                JeMistoPodnikaniStejne.send_keys(webdriver.common.keys.Keys.SPACE)

            else:
                try:
                    MistoPodnikani_Ulice = web.find_element_by_name(
                        "PravnickaOsoba.MistoPodnikani.Ulice"
                    )
                    MistoPodnikani_Ulice.send_keys(data[12])

                except:
                    print("Místo podnikání - ulice nebyla vyplněna")

                try:
                    MistoPodnikani_CisloPopisne = web.find_element_by_name(
                        "PravnickaOsoba.MistoPodnikani.CisloPopisne"
                    )
                    MistoPodnikani_CisloPopisne.send_keys(data[13])

                except:
                    print("Místo podnikání - číslo popisné nebylo vyplněno")

                try:
                    MistoPodnikani_CisloOrientacni = web.find_element_by_name(
                        "PravnickaOsoba.MistoPodnikani.CisloOrientacni"
                    )
                    MistoPodnikani_CisloOrientacni.send_keys(data[14])

                except:
                    print("Místo podnikání - číslo orientační nebylo vyplněno")

                try:
                    MistoPodnikani_Obec = web.find_element_by_name(
                        "PravnickaOsoba.MistoPodnikani.Obec"
                    )
                    MistoPodnikani_Obec.send_keys(data[15])

                except:
                    print("Místo podnikání - obec nebyla vyplněna")

                try:
                    MistoPodnikani_PSC = web.find_element_by_name(
                        "PravnickaOsoba.MistoPodnikani.PSC"
                    )
                    MistoPodnikani_PSC.send_keys(data[16])

                except:
                    print("Místo podnikání - PSČ nebylo vyplněno")

                try:
                    MistoPodnikani_Kraj = Select(
                        web.find_element_by_name("PravnickaOsoba.MistoPodnikani.Kraj")
                    )
                    MistoPodnikani_Kraj.select_by_visible_text(data[17])

                except:
                    print("Místo podnikání - kraj nebyl vyplněn")

        except:
            print("Místo podníkání je stejné nebylo zvoleno")

        try:
            ZodpovednaOsobaList_FunkceVSpolecnosti = web.find_element_by_xpath(
                "//select[contains(@id, 'FunkceVSpolecnosti')]"
            )
            ZodpovednaOsobaList_FunkceVSpolecnosti.send_keys(data[18])

        except:
            print("Zodpovědná osoba - funkce ve společnosti nebyla vyplněna")

        try:
            ZodpovednaOsobaList_TitulPredJmenem = web.find_element_by_xpath(
                "//input[contains(@id, 'TitulPredJmenem')]"
            )
            ZodpovednaOsobaList_TitulPredJmenem.send_keys(data[19])

        except:
            print("Zodpovědná osoba - titul před jménem nebyl vyplněn")

        try:
            ZodpovednaOsobaList_TitulZaJmenem = web.find_element_by_xpath(
                "//input[contains(@id, 'TitulZaJmenem')]"
            )
            ZodpovednaOsobaList_TitulZaJmenem.send_keys(data[20])

        except:
            print("Zodpovědná osoba - titul za jménem nebyl vyplněn")

        try:
            ZodpovednaOsobaList_Jmeno = web.find_element_by_xpath(
                "//input[contains(@id, 'Jmeno')]"
            )
            ZodpovednaOsobaList_Jmeno.send_keys(data[21])

        except:
            print("Zodpovědná osoba - jméno nebylo vyplněno")

        try:
            ZodpovednaOsobaList_Prijmeni = web.find_element_by_xpath(
                "//input[contains(@id, 'Prijmeni')]"
            )
            ZodpovednaOsobaList_Prijmeni.send_keys(data[22])

        except:
            print("Zodpovědná osoba - příjmení nebylo vyplněno")

        try:
            Kontakt_Telefon1 = web.find_element_by_name("Kontakt4.Telefon1")
            Kontakt_Telefon1.send_keys(data[43])

        except:
            print("Kontakt - hlavní telefon nebyl vyplněn")

        try:
            Kontakt_Telefon2 = web.find_element_by_name("Kontakt4.Telefon2")
            Kontakt_Telefon2.send_keys(data[44])

        except:
            print("Kontakt - vedlejší telefon nebyl vyplněn")

        try:
            Kontakt_Email = web.find_element_by_name("Kontakt4.Email")
            Kontakt_Email.send_keys(data[45])

        except:
            print("Kontakt - email nebyl vyplněn")

        try:
            BankovniSpojeni_CisloUctu = web.find_element_by_name(
                "BankovniSpojeni.CisloUctu"
            )
            BankovniSpojeni_CisloUctu.send_keys(data[46])

        except:
            print("Bankovní spojení - číslo účtu nebylo vyplněno")

        try:
            BankovniSpojeni_KodBanky = web.find_element_by_name(
                "BankovniSpojeni.KodBanky"
            )
            BankovniSpojeni_KodBanky.send_keys(data[47])

        except:
            print("Bankovní spojení - kód banky nebyl vyplněn")

        try:
            ObchodniRejstrik_ORZapis = web.find_element_by_name(
                "ObchodniRejstrik.ORZapis"
            )
            ObchodniRejstrik_ORZapis.send_keys(data[48])

        except:
            print("Obchodní rejstřík - spisová značka nebyla vyplněna")

        try:
            ObchodniRejstrik_ORVydal = web.find_element_by_name(
                "ObchodniRejstrik.ORVydal"
            )
            ObchodniRejstrik_ORVydal.send_keys(data[49])

        except:
            print("Obchodní rejstřík - příslušný krajský soud nebyl vyplněnen")

        try:
            ObchodniRejstrik_ORDatum = web.find_element_by_name(
                "ObchodniRejstrik.ORDatum"
            )
            ObchodniRejstrik_ORDatum.send_keys(data[50])

        except:
            print("Obchodní rejstřík - datum vydání nebyl vyplněn")

        try:
            if data[51] == "Ano":
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
                    PlanovaneUkonceni_UkonceniCinnostiDatum.send_keys(data[52])

                except:
                    print("Plánované ukončení - datum ukončení činnosti nebyl vyplněn")

        except:
            print("Ukončení činnosti nebylo zvoleno")

        try:
            if data[53] == "Ano":
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
                    PlanovanyProdej_ProdejPodnikuDatum.send_keys(data[54])

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
            UverInvesticni_VyseUveru.send_keys(data[55])

        except:
            print("Úvěr investiční - výše úvěru nebyla vyplněna")

        try:
            UverInvesticni_DobaSplatnosti = web.find_element_by_name(
                "UverInvesticni.DobaSplatnosti"
            )
            UverInvesticni_DobaSplatnosti.send_keys(data[56])

        except:
            print("Úvěr investiční - doba splatnosti nebyla vyplněna")

        try:
            UverInvesticni_OdkladSplatky = web.find_element_by_name(
                "UverInvesticni.OdkladSplatky"
            )
            UverInvesticni_OdkladSplatky.send_keys(data[57])

        except:
            print("Úvěr investiční - odklad splátky nebyl vyplněn")

        try:
            UverInvesticni_ZduvodneniOdkladuInvesticni = web.find_element_by_name(
                "UverInvesticni.ZduvodneniOdkladuInvesticni"
            )
            UverInvesticni_ZduvodneniOdkladuInvesticni.send_keys(data[58])

        except:
            print("Úvěr investiční - zdůvodnění odkladu splátky nebylo vyplněno")

        try:
            if data[59] == "Ne":
                jeSnizeni = web.find_element_by_name("jeSnizeni")
                jeSnizeni.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Snížení jistiny nebylo zvoleno")

        try:
            if data[60] == "Ano":
                jeZacinajici = web.find_element_by_name("jeZacinajici")
                jeZacinajici.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Začínající podnikatel nebyl zvolen")

        try:
            CestneProhlaseniTicket = web.find_element_by_name("CestneProhlaseniTicket")
            CestneProhlaseniTicket.send_keys(webdriver.common.keys.Keys.SPACE)

        except:
            print("Čestné prohlášení nebylo zvoleno")

        # TEST PROMĚNNÝCH
        # print(" ")
        # print("----------------------------------------")
        # print("TEST PROMĚNNÝCH")
        # print("----------------------------------------")
        # print(" ")
        # print("ObchodniJmeno: ", data[0])
        # print("TypPO: ", data[1])
        # print("Plátce DPH: ", data[2])
        # print("IČ: ", data[3])
        # print("DIČ: ", data[4])
        # print("SidloSpolecnosti.Ulice: ", data[5])
        # print("SidloSpolecnosti.CisloPopisne: ", data[6])
        # print("SidloSpolecnosti.CisloOrientacni: ", data[7])
        # print("SidloSpolecnosti.Obec: ", data[8])
        # print("SidloSpolecnosti.PSC: ", data[9])
        # print("SidloSpolecnosti.Kraj: ", data[10])
        # print("JeMistoPodnikaniStejne: ", data[11])
        # print("MistoPodnikani.Ulice: ", data[12])
        # print("MistoPodnikani.CisloPopisne: ", data[13])
        # print("MistoPodnikani.CisloOrientacni: ", data[14])
        # print("MistoPodnikani.Obec: ", data[15])
        # print("MistoPodnikani.PSC: ", data[16])
        # print("MistoPodnikani.Kraj: ", data[17])
        # print("ZodpovednaOsobaList.FunkceVSpolecnosti: ", data[18])
        # print("ZodpovednaOsobaList.TitulPredJmenem: ", data[19])
        # print("ZodpovednaOsobaList.TitulZaJmenem: ", data[20])
        # print("ZodpovednaOsobaList.Jmeno: ", data[21])
        # print("ZodpovednaOsobaList.Prijmeni: ", data[22])
        # print("ZodpovednaOsobaList.FunkceVSpolecnosti2: ", data[23])
        # print("ZodpovednaOsobaList.TitulPredJmenem2: ", data[24])
        # print("ZodpovednaOsobaList.TitulZaJmenem2: ", data[25])
        # print("ZodpovednaOsobaList.Jmeno2: ", data[26])
        # print("ZodpovednaOsobaList.Prijmeni2: ", data[27])
        # print("ZodpovednaOsobaList.FunkceVSpolecnosti3: ", data[28])
        # print("ZodpovednaOsobaList.TitulPredJmenem3: ", data[29])
        # print("ZodpovednaOsobaList.TitulZaJmenem3: ", data[30])
        # print("ZodpovednaOsobaList.Jmeno3: ", data[31])
        # print("ZodpovednaOsobaList.Prijmeni3: ", data[32])
        # print("ZodpovednaOsobaList.FunkceVSpolecnosti4: ", data[33])
        # print("ZodpovednaOsobaList.TitulPredJmenem4: ", data[34])
        # print("ZodpovednaOsobaList.TitulZaJmenem4: ", data[35])
        # print("ZodpovednaOsobaList.Jmeno4: ", data[36])
        # print("ZodpovednaOsobaList.Prijmeni4: ", data[37])
        # print("ZodpovednaOsobaList.FunkceVSpolecnosti5: ", data[38])
        # print("ZodpovednaOsobaList.TitulPredJmenem5: ", data[39])
        # print("ZodpovednaOsobaList.TitulZaJmenem5: ", data[40])
        # print("ZodpovednaOsobaList.Jmeno5: ", data[41])
        # print("ZodpovednaOsobaList.Prijmeni5: ", data[42])
        # print("Kontakt4.Telefon1: ", data[43])
        # print("Kontakt4.Telefon2: ", data[44])
        # print("Kontakt4.Email: ", data[45])
        # print("BankovniSpojeni.CisloUctu: ", data[46])
        # print("BankovniSpojeni.KodBanky: ", data[47])
        # print("ObchodniRejstrikFyzicka.ORZapis: ", data[48])
        # print("ObchodniRejstrikFyzicka.ORVydal: ", data[49])
        # print("ObchodniRejstrikFyzicka.ORDatum: ", data[50])
        # print("PlanovaneUkonceni.UkonceniCinnosti: ", data[51])
        # print("PlanovaneUkonceni.UkonceniCinnostiDatum: ", data[52])
        # print("PlanovanyProdej.ProdejPodniku: ", data[53])
        # print("PlanovanyProdej.ProdejPodnikuDatum: ", data[54])
        # print("UverInvesticni.VyseUveru: ", data[55])
        # print("UverInvesticni.DobaSplatnosti: ", data[56])
        # print("UverInvesticni.OdkladSplatky: ", data[57])
        # print("UverInvesticni.ZduvodneniOdkladuInvesticni: ", data[58])
        # print("jeSnizeni: ", data[59])
        # print("jeZacinajici: ", data[60])

        time.sleep(3600)