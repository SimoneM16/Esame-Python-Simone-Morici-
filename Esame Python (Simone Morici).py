# Importo il file relativo ai casi nel mondo e lo converto in una tabella con Pandas
import pandas as pd

Raw=pd.read_csv(r"C:\Users\simon\Downloads\owid-covid-data.csv") # Da sostituire con il percorso usato nel proprio pc

Tabella=pd.DataFrame(Raw)

print("\n")

### Esercizio n°1 ###
print("Esercizio n°1")

print("Il numero di righe del dataset è ",Tabella.shape[0],"ed il numero di colonne è ", Tabella.shape[1]) # Visualizzo le dimensioni del dataset

print("\n")

### Esercizio n°2 ###
print("Esercizio n°2")

Continenti=["Asia","North America","South America","Europe","Oceania","Africa"] # Definisco una lista di continenti

Casi_totali=0 # Inizializzo a 0 i casi totali per poterli contare nel ciclo successivo

for N in Continenti:                                                # Per ciascun continente calcolo la somma dei nuovi casi ogni giorno per ottenere i casi totali
    X=Tabella.loc[Tabella["continent"] == N, "new_cases"].sum() 
    print("I casi totali in ",N, "sono stati ",int(X))
    Casi_totali=Casi_totali+X
    
print("\n")

### Esercizio n°3 ###
print("Esercizio n°3")

print("I casi totali nel mondo sono stati ",int(Casi_totali))

print("\n")

print("La percentuale, rispetto ai casi totali nel mondo, per ciascun continente è:")
for N in Continenti:                                                # Per ciascun continente calcolo i casi totali e li divido per i casi totali nel mondo
    X=Tabella.loc[Tabella["continent"] == N, "new_cases"].sum() 
    print(N, ":",int(round((X/Casi_totali)*100,0)),"%")                 # Esprimo il risultato in percentuale

print("\n")

for N in Continenti:                                                        # Calcolo il numero massimo di casi giornalieri avuti in ciascun continente
    Massimo=Tabella.loc[Tabella['continent'] == N, 'new_cases'].max()
    print("Il massimo numero di casi giornalieri in ",N," è stato ",int(Massimo))
    
print("\n")

for N in Continenti:                                                        # Calcolo la media di casi giornalieri avuti in ciascun continente
    Media=Tabella.loc[Tabella['continent'] == N, 'new_cases'].mean()
    print("La media di casi giornalieri in ",N," è stata ",int(Media))
    
print("\n")
    
###Esercizio 4###

Y=Tabella.loc[Tabella['location'] == "Italy", "total_cases"]   # Raggruppo i casi totali in Italia
X=Tabella.loc[Tabella['location'] == "Italy", "date"]          # Raggruppo le rispettive date


import matplotlib.pyplot as plt   # Credo il grafico
plt.tick_params(bottom=False)     # Non riesco a visualizzare correttamente le date (sono troppe e non riesco a visulizzarne solo alcune) e perciò le cancello
plt.plot(X,Y)
plt.xlabel("Data")
plt.ylabel("Contagi Totali")
plt.title("Evoluzione contagi in Italia")
plt.show()




    




