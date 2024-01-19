import csv

def izdrukaj_otro_kolonnu(file_path, delimiter=','):
    try:
        with open(file_path, 'r', encoding='utf-8') as faila_atslega:
            lasitajs = csv.reader(faila_atslega, delimiter=delimiter)
            
            for rinda in lasitajs:
                if len(rinda) >= 2:
                    print(rinda[1])
    except FileNotFoundError:
        print(f"Faila '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

faila_ceels = 'jusu_faila_ceels.csv'
izdrukaj_otro_kolonnu(faila_ceels)
