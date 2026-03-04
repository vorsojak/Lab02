import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")


    txtIn = input("Seleziona l'opzione: ")
    try:
         int(txtIn)
    except (TypeError, ValueError) as e:
        print(f"Input non valido, scegli un opazione da 1 a 5!")
        continue

    if int(txtIn) == 1:
        while True:
            print()
            txtIn = input("Inserisci la nuova parola nel formato 'parolaAliena Traduzione'."
                          " Se vuoi tornare al menu clicca +.\n").strip()
            if txtIn == "+":
                break
            txtIn = txtIn.split()
            if len(txtIn) != 2:
                print("Errore: formato errato!")
                continue
            else:
                t.handleAdd(txtIn)
        continue
    if int(txtIn) == 2:
        while True:
            print()
            txtIn = input("Inserisci la parola aliena da cercare."
                          " Se vuoi tornare al menu clicca +.\n").strip()
            if txtIn == "+":
                break
            t.handleTranslate(txtIn)
        continue

    if int(txtIn) == 3:
        while True:
            print()
            txtIn = input("Inserisci la parola aliena con WildCard da cercare (es. par?la)."
                          " Se vuoi tornare al menu clicca +.\n").strip()
            if txtIn == "+":
                break
            t.handleWildCard(txtIn)
        continue
    if int(txtIn) == 4:
        t.stampDictionary()
        pass
    if int(txtIn) == 5:
        print("Ciao!")
        break