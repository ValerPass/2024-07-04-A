a. Permettere all’utente di scegliere da un menù a tendina un anno tra tutti i possibili anni in cui 
ci sono stati avvistamenti (ordinati in senso DECRESCENTE).
b. Popolare il menù a tendina Forma con tutte le possibili forme, prese dalla colonna “shape” del db, 
relative agli avvistamenti nell’anno considerato (escludendo i casi in cui non è specificata nessuna forma, 
ordinati alfabeticamente).
c. Facendo click sul bottone CREA GRAFO, creare un grafo orientato e non pesato, i cui vertici siano tutti 
gli avvistamenti presenti nella tabella “sighting” che siano avvenuti nell’anno selezionato dall’utente e con 
la shape desiderata. Il grafo è un grafo diretto, ed un arco fra due avvistamenti esiste se e solo se tali 
avvistamenti sono avvenuti nello stesso stato. L’arco è uscente dall’avvistamento che è avvenuto temporalmente prima ed 
entrante nell’avvistamento avvenuto dopo.
d. Stampare il numero di componenti debolmente connesse. Inoltre, identificare la componente connessa di dimensione 
maggiore, e stamparne i nodi – includendo il dettaglio della città in cui è avvenuto l’avvistamento e la data.
