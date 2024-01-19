def lasit_un_drukat(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as faila_atslega:
            saturs = faila_atslega.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

faila_cels = 'jusu_faila_cels.txt'
lasit_un_drukats(faila_cels)
