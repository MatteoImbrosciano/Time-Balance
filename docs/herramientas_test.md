## Criteri di Selezione

Alcuni prerequisiti per la scelta delle librerie:

- Deve avere un buon punteggio su snyk Advisor. Avere un buon punteggio su Skyk Advisor implica che lo strumento soddisfa standard elevati in ambiti quali la sicurezza dei dati e la gestione dei rischi, dimostrandosi un buon strumento destinato all'utilizzo in un repository.
- In definitiva, verrà valorizzato lo strumento che comprende una maggiore varietà di asserzioni, permettendoci una maggiore varietà nell'esecuzione dei diversi test.

I prerequisiti per la scelta di un test runner saranno simili a quelli della libreria di asserzioni:

- Deve avere un buon punteggio su snyk Advisor. Avere un buon punteggio su Skyk Advisor implica che lo strumento soddisfa standard elevati in ambiti quali la sicurezza dei dati e la gestione dei rischi, dimostrandosi un buon strumento destinato all'uso in un repository/progetto.
- Infine, verrà valutata la scalabilità del test runner nel caso in cui il progetto diventi più complesso nelle future Milestones. In questa scalabilità verranno valorizzate funzionalità come: un sistema di dispositivi e risultati dettagliati, facilitando il debugging quando ci sono molti errori in un grande progetto.
  
## Analisi delle Opzioni

### Librerie di asserzioni esaminate

1. **unittest (PyUnit)**
   - Link Snyk: (https://snyk.io/advisor/python/unittest)
   - Inclusa nella libreria standard di Python, garanzia di manutenzione e aggiornamenti.
   - Set di asserzioni limitato, ma sicuro e affidabile.

3. **behave**  
   - Link Snyk: [https://snyk.io/advisor/python/behave](https://snyk.io/advisor/python/behave)  
   - Orientata al BDD, ma valutazione su Snyk e manutenzione non soddisfacenti.
   - Non adatta per esigenze di lungo termine.

4. **ensure**  
   - Link Snyk: [https://snyk.io/advisor/python/ensure](https://snyk.io/advisor/python/ensure)  
   - Punteggio non adeguato su Snyk Advisor.  
   - Non garantisce gli standard di sicurezza richiesti.

5. **grappa**  
   - Link Snyk: [https://snyk.io/advisor/python/grappa](https://snyk.io/advisor/python/grappa)  
   - Bassa valutazione e manutenzione non ottimale.
   
6. **PyHamCrest**  
   - Link Snyk: [https://snyk.io/advisor/python/pyhamcrest](https://snyk.io/advisor/python/pyhamcrest)  
   - Non offre le garanzie di manutenzione e sicurezza necessarie.

**Scelta finale per le librerie di asserzioni:**  
Le opzioni esterne non garantiscono gli standard di sicurezza e manutenzione richiesti. `unittest`, come libreria standard, fornisce un supporto affidabile e continuo. Tuttavia, per test più complessi (ad esempio gestione di warning o asserzioni più espressive), si potrà integrare l’uso delle asserzioni di `pytest` e l’`assert` nativo di Python, ampliando così la gamma di test possibili senza perdere stabilità.

### Test Runner esaminati

1. **unittest come test runner**  
   - Integrato, ma senza fixture evolute né output dettagliato.
   - Non soddisfa i requisiti di scalabilità.

2. **pytest**  
   - Link Snyk: [https://snyk.io/advisor/python/pytest](https://snyk.io/advisor/python/pytest)  
   - Ottime valutazioni su Snyk, comunità attiva, aggiornamenti frequenti.
   - Fixture integrate, output chiaro, rilevamento automatico dei test, supporto a molti plugin.
   
3. **Nose2**  
   - Link Snyk: [https://snyk.io/advisor/python/nose2](https://snyk.io/advisor/python/nose2)  
   - Valutazioni non ideali. Non offre vantaggi rispetto a pytest.

**Scelta finale del test runner:**  
`pytest` è la scelta ottimale: garantisce la sicurezza, la flessibilità e la scalabilità necessarie. L’integrazione con asserzioni semplici (`assert`) e la presenza di fixture semplificano il testing, rendendo più agile la crescita futura del progetto.

## Conclusione

La configurazione finale è dunque:

- **Libreria di asserzioni:** `unittest` come base, arricchita quando necessario con asserzioni di `pytest` e l’`assert` nativo di Python, per garantire una gamma più ampia di test.
- **Test Runner:** `pytest`, per sfruttare la sua versatilità, le fixture integrate, il supporto della community, l’output chiaro e la buona valutazione di sicurezza su Snyk Advisor.

Questa combinazione consente di mantenere un equilibrio tra stabilità, sicurezza, varietà di test e capacità di gestione di scenari complessi, favorendo uno sviluppo sostenibile del progetto nel tempo.

## Comandi principali per il testing
Il progetto utilizza `pytest` come test runner. I comandi principali per eseguire i test e analizzare la copertura del codice sono documentati di seguito:

1. **Eseguire tutti i test:**
   ```bash
   poetry run poe test
