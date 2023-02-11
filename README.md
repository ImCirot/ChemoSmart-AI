# ChemoSmart-AI
Modulo di Intelligenza Artficiale sviluppato per il sistema ChemoSmart per il progetto di Fondamenti di Intelligenza Artificiale

- Ciro Troiano Mat. 0512111005
- Antonio Nappi Mat. 0512112859
- Giuseppe Basile Mat. 0512109979
- Mihail Purice Mat. 0512110819

<h2>Il progetto</h2>
Gli appuntamenti chemioterapici al giorno d'oggi vengono schedulati sulla base di euristiche ben note che favoriscono, principalmente, la riduzione dello spreco dei farmaci. Il sistema nasce dalla necessità e dalla voglia di fornire un ulteriore "caratterizzazione" per la schedulazione degli appuntamenti.<br>
Il modulo di IA qui presente, utilizza informazioni della storia clinica presente, e passata, del paziente per fornire un sistema di priorità utile alla schedulazione.<br>
Cosi facendo, il sistema è in grado di supportare il personale dedito ma, allo stesso tempo, i pazienti stessi.
<br><br>
<h3>Il dataset</h3>
Il modello è stato realizzato partendo da un dataset pubblico disponibile sulla piattaforma Kaggle al link: https://www.kaggle.com/datasets/rishidamarla/cancer-patients-data
<br><br>
<h3>Analisi del dataset</h3>
Le caratteristiche presenti nel dataset sono state analizzate utilizzando la libreria <b>Pandas</b> per l'accesso al dataset e alle sue caratteristiche, la libreria <b>seaborn</b>, utilizzata per realizzare i grafici che mostrano correlazione fra le caratteristiche del dataset e il valore risultate e, infine, la libreria <b>matlplotlib</b>, in particolare il modello <b>pyplot</b>, per poter impostare e visualizzare i grafici realizzati.
<br><br>
<h3>Il modello</h3>
Il problema, sulla base del dataset fornito, è stato trattato come un problema di <b>classificazione</b>.<br>
Il modello è stato realizzato utilizzando un sia un algoritmo <b>Decisional Tree</b> che un algoritmo <b>Naive Bayes</b>. Infine, si sono testati i risultati ottenuti dai due modelli e scelto il "migliore" per il problema posto in essere.<br><br>
I modelli sono stati realizzati utilizzando <b>Python</b> e, in particolare, glii algoritmi utilizzati, cosi come le strategie per training e validazione del modello, sono disponibili nella libreria <b>Scikit-Learn</b>, libreria disponibile per più linguaggi di programmazione.
