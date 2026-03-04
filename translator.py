import fnmatch
from dataclasses import dataclass


@dataclass
class Translator:

    def __init__(self):
        self.dizionario = {}
        dizionario: dict

    def printMenu(self):
        # 1. Aggiungi nuova parola
        print("1. Aggiungi una nuova parola")
        # 2. Cerca una traduzione
        print("2. Cerca una traduzione")
        # 3. Cerca con wildcard
        print("3. Cerca con wildcard")
        # 4. Stampa tutto il dizionario
        print("4. Stampa tutto il dizionario")
        # 5. Exit
        print("5. Exit")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="utf-8") as f:
            for r in f:
                riga = r.strip().split()
                #print(riga)
                parolaAliena = riga[0]
                parolaItaliana = riga[1]
                self.dizionario[parolaAliena] = parolaItaliana
            #print(self.dizionario)
        return self.dizionario

    def handleAdd(self, entry):
        self.dizionario[entry[0]] = entry[1]
        with open("dictionary.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{entry[0]} {entry[1]}")

        print(f"{entry[0]} correttamente aggiunta al dizionario!")
        return


    def handleTranslate(self, query):
        traduzione = self.dizionario.get(query)
        if traduzione is None:
            print("Parola non presente nel dizionario.")
            return
        print(f"La traduzione di {query} è {traduzione}.")
        return

    def handleWildCard(self,query):
        for k, v in self.dizionario.items():
            if fnmatch.fnmatch(k, query):
                print(f"Parola trovata: {k}. La traduzione è {v}.")
                return
        print("Nessuna parola trovata")
        return

    def stampDictionary(self):
        for k,v in self.dizionario.items():
            print(f"{k} - {v}")