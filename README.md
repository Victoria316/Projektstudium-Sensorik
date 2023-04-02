# Projektstudium-Sensorik
 
Definieren Sie die Anforderungen an die Software:

Was soll die Software tun?
- Siehe Anforderungen: <REF> TODO @DOKU
Welche Funktionen muss sie haben?
- Siehe UmL Diagramm:  <REF> TODO @DOKU ENTWICKLER 

1. Definieren Sie die Art der Daten, die die Software sammeln und analysieren soll.

wie werden die Daten aufgenommen und gespeichert?
-  in einer Flask Session 
-  Textfelder
-  Matching 
-  Multiple Choice 
-  Bitte ergänzen falls jemanden was auffällt.

-> Speichern in einer CSV oder Excel Tabelle (Docx) ||| bei jeder Antwort updaten? 
-> Optional in Dataframe (Pandas) ||| was passiert bei vorzeitigen Ende einer Session? 

2. Bestimmen Sie die Methoden zur Analyse der Daten:
Wie sollen die Daten verarbeitet und ausgewertet werden?
    Vielleicht extra Script für Auswertung activierung bei  press Button der letzten Abgabe. 
-  File einlesen 
-  Auswertung mit Matplotlib, Numpy , Pandas --> Möglichkeit Graphen und ähnliches zuerstellen  
-

3. Erstellen Sie ein Design für die Software

Wie soll die Benutzeroberfläche aussehen?
- Webapplikation 
-> Welche Hierauchie wird durchlaufen 
zb. Anmeldung (kein Login nur Name für die Auswertung zwecks Filename) 
    -> Zusammenstellung des Quizes (eventuell schon vorgegeben? oder Direkt Auswahl für jeden oder nur für User xxx )  
    -> Erste Aufgabe -> OnKlick Abgabe (Update) -> nächste Aufgabe -> ... Ende Screen evtl mit Auswertung? 
    
welche Funktionen sollen verfügbar sein?
- Zusammenstellen von Aufgabentypen eines Themabereichs 
    -> Atomisieren der Aufgaben und Unterteilung in Themengebiete 
    -> SQL würde sich anbieten wegen Primär Fremdschlüssel  Relationen , CSV Format kann für Multiple Choice und ähnliches benutzt werden. 
    -> Pro Aufgabentyp eine Klasse bauen die sie erstellt <-> Daten müssen in einer bestimmten Form vorlegen
    -> Api von Python für Googleforms -> kein strunz was da Rauskommt 

4. Implementieren Sie die Software
Flask Session -> Html Page -> Database(As needed) -> Script zur Erstellung von Aufgabentypen -> Script zur Auswertung 

siehe Flask Ablauf Diagramm @All 
siehe Html beispiele 
siehe Database Design 
Scripts immer mit DOC STRING UND COMMENT (Chat Bot kann da gut helfen)

5. Testen Sie die Software: -> Student aus Praktikum 

TODO BUG: < Ref Bug fix >
- Line, Filename und Kurzbeschreibung


6. Optimieren Sie die Software: Verbessern Sie die Leistung der Software und beheben Sie alle Fehler oder Probleme, die während des Testens aufgetreten sind.
