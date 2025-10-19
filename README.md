<h1>FastAPI_Sevilla</h1>

<h2>Activitat FastAPI Basics</h2>
    <p>
        En primer lloc, el codi emprat per a la creació dels endpoints requerits és el següent:
    </p>
    <img src="images/codigo1.PNG" alt="Imatge del codi de l'activitat">
    <img src="images/codigo2.PNG" alt="Imatge del codi de l'activitat">
    <p>
        Tal com es pot veure tenim una llita d'usuaris, i una funció que el que fa és convertir aquesta llista a diccionari. He fet la funció "passarADict" per tal d'estalviar-me codi, i redundància, en els diferents endpoints.
        En el moment d'executar-ho amb la documentació de FastAPI, Swagger, ens donaria aquest resultat:
    </p>
    <img src="images/ui.PNG" alt="Imatge visual de Swagger">
    <p>
        A partir d'aqui, anem veient qué fa individualment cada endpoint.
    </p>
    <h3>Crear - Afegir a la list</h3>
        <p>
            En primer lloc, volem que, mitjançant el mètode POST, es puguin crear usuaris nous i afegir-los a la llista. Per paràmetres demanem un nom, que serà el nom del nou usuari, i l'afegirà a la llista.     
        </p>
        <img src="images/1.0.PNG" alt="Imatge sobre crear usuari">
        <img src="images/1.1.PNG" alt="Imatge sobre crear usuari">
        <p>
            En aquest cas, farem clic a "Try it out" i afegirem l'usuari "Lucía":
        </p>
        <img src="images/1.2.PNG" alt="Imatge sobre crear usuari">
        <p>
            Posteriorment, mitjançant la funció que he comentat abans es convertirà la llista, amb el nou usuari, a diccionari, i finalment retornarà aquest diccionari.
        </p>
        <img src="images/1.3.PNG" alt="Imatge sobre crear usuari">
        <img src="images/1.4.PNG" alt="Imatge sobre crear usuari">
    <h3>Llegir - Consultar un usuari/objecte de la llista</h3>
        <p>
            Ara mitjançant el mètode GET, volem consultar un usuari de la llista tot introduint el seu ID. Per aquest mètode he fet servir un condicional per tal que si l'ID introduït no existeix, doni un missatge d'error. En cas que sí que existeixi, sí que es podrà consultar l'usuari en qüestió.
        </p>
        <img src="images/2.0.PNG" alt="Imatge sobre consultar un usuari">
        <img src="images/2.1.PNG" alt="Imatge sobre consultar un usuari">
        <p>
            Com hem fet abans, li donarem a "Try it out" i introduirem l'ID en qüestió, en aquest cas el "2":
        </p>
        <img src="images/2.2.PNG" alt="Imatge sobre consultar un usuari">
    <h3>Llegir - Consultar tots els usuaris</h3>
        <p>
            Ara volem, mitjançant el mètode GET llegir tots els usuaris. Un cop li donem a executar ens apareixerà la llista dels usuaris, amb l'usuari Lucía anteriorment afegida.
        </p>
        <img src="images/3.0.PNG" alt="Imatge sobre consultar tots els usuaris">
        <img src="images/3.2.PNG" alt="Imatge sobre consultar tots els usuaris">
        <img src="images/3.3.PNG" alt="Imatge sobre consultar tots els usuaris">
    <h3>Actualitzar - Actualització completa</h3>
        <p>
            En aquest punt el que es pretén és que, mitjançant el mètode PUT, puguem actualitzar un usuari de la llista.
            Tal com passava amb la consulta individual per ID, en aquest punt he fet un condicional que, en cas que l'ID no estigui, doni un missatge error. En canvi, en cas que l'ID que donem sí que existeixi, actualitzarà el nom de l'usuari en qüestió, pel que volguem. 
        </p>
        <img src="images/4.0.PNG" alt="Imatge sobre actualitzar un usuari">
        <img src="images/4.1.PNG" alt="Imatge sobre actualitzar un usuari">
        <p>
            En la següent captura es pot veure què passaria si m volem canviar-li el nom a un ID, el 5, que no existeix a la llista:
        </p>
        <img src="images/4.3.PNG" alt="Imatge sobre actualitzar un usuari">
        <p>
            En canvi, si ho fem amb un ID que sí que existeix, per exemple, el 0, actualitzant el seu nom de "Adrián" a "Adrià":
        </p>
        <img src="images/4.2.PNG" alt="Imatge sobre actualitzar un usuari">
    <h3>Eliminar - Esborrar usuari</h3>
        <p>
            Finalment, si volem esborrar un usuari, ho farem amb el mètode DELETE:
        </p>
        <img src="images/5.0.PNG" alt="Imatge sobre borrar un usuari">
        <p>
            Actualment tenim aquesta llista d'usuaris:
        </p>
        <img src="images/5.1.PNG" alt="Imatge sobre borrar un usuari">
        <p>
            Haurem d'introduir el ID de l'usuari que volem esborrar, i com en els casos anteriors, si introduïm un ID que no existeix, ens sortirà un missatge d'error:
        </p>
        <img src="images/5.2.PNG" alt="Imatge sobre borrar un usuari">
        <p>
            En canvi, si volem eliminar un ID, per exemple el 2, funcionarà perfectament, i ens esborrarà l'usuari en qüestió. I a més, ara, Lucía passarà de ser l'ID 3, a ser la 2.
        </p>
        <img src="images/5.3.PNG" alt="Imatge sobre borrar un usuari">