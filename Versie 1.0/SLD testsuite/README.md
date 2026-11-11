# Tests voor de SLD controle-XSLT's

Controleert na een aanpassing aan een van de SLD-controle-XSLT's of er niets is omgevallen, voor **elke SIKB0101-versie** (nu 14.9.0 en 15.0). Zelfde opzet, controles en rapport als de SAD-testsuite.

## Opzet

```
Versie 1.0/
├── SLD_Extern_Uitwisselberichten/         ← geleverde versie 14.9.0 (ongewijzigd, niets van de tests erin)
│   └── Controle XSLT/ , Voorbeeldberichten/inname, Voorbeeldberichten/uitgifte, XSD/
├── SLD_Extern_Uitwisselberichten v15.0/   ← geleverde versie 15.0 (idem)
├── SLD_Intern_Uitwisselberichten/         ← geen Controle XSLT → wordt niet getest
└── SLD testsuite/                         ← ALLES voor de tests
    ├── run_tests.py                       ← de testrunner
    ├── run_alle_versies.bat               ← dubbelklik: test alle versies
    ├── suite.json                         ← SLD-instellingen: mappen, XSD's, welk bericht naar welke XSLT
    ├── cases.json                         ← handgeschreven testcases (voor alle versies)
    ├── nieuwe_versie.py, maak_testberichten.py, fetch_schemas.py, xslt_sites.py, schema-cache/
    └── versies/
        ├── SLD_Extern_Uitwisselberichten/         ← zelfde naam als de geleverde map
        │   ├── run_tests.bat                      ← dubbelklik: test alleen deze versie
        │   ├── versie.json                        ← versie-afhankelijke waarden voor cases.json
        │   ├── bekende_afwijkingen.json, overrides.json, onbereikbaar.json
        │   ├── baseline/ , testberichten/
        │   └── report/report.html                 ← rapport van de laatste run
        └── SLD_Extern_Uitwisselberichten v15.0/   ← (zelfde opbouw)
```

De geleverde mappen blijven precies zoals ze geleverd zijn. De runner koppelt ze **op mapnaam**: een map naast `SLD testsuite` met een `Controle XSLT`-map wordt getest als er een gelijknamige map in `SLD testsuite/versies/` staat. Elke versie gebruikt **zijn eigen** XSLT's, voorbeeldberichten en XSD's. Een geleverde map zonder testconfiguratie (of een configuratie zonder geleverde map) wordt overgeslagen met een melding.

## Welk bericht gaat door welke XSLT?

SLD heeft vier controle-XSLT's. Welke bij een bericht hoort, hangt af van het **soort bericht** (het element in `sourceDocument`) en de **kwaliteit** (`qualityRegime`). Dat staat in `suite.json` onder `controles`; de eerste regel die past wint:

| sourceDocument | qualityRegime | Controle (XSLT) |
|---|---|---|
| `SLD_CompleteReport` | IMBRO | OW Complete Report (`SIKB_SLD OW Complete Report.xslt`) |
| `SLD_CompleteReport`, `SLD_StartReport` | IMBRO/A | WBB Complete Report + Start Report |
| `SLD_ChangeSoilLocationData` | IMBRO/A | WBB Change SoilLocation |
| `SLD_NewDecision` | IMBRO/A | WBB New Decision |
| `SLD_SoilLocationFinalisation` | – | geen controle-XSLT → *overgeslagen* (bevat geen SIKB-inhoud) |

Komt er een nieuwe XSLT of berichtsoort bij, dan voeg je een regel toe aan `suite.json`.

## Installeren (eenmalig)

Nodig: Python 3 (met *Add python.exe to PATH*). De `.bat`-bestanden controleren zelf of de pakketten `saxonche` en `lxml` aanwezig zijn en installeren ze anders eenmalig (`requirements.txt`). Handmatig kan ook:

```
python -m pip install --user -r requirements.txt
python fetch_schemas.py
```

`saxonche` is Saxon-HE (XSLT 2.0-processor, van Saxonica, open source onder MPL 2.0), `lxml` (BSD-licentie) wordt gebruikt voor XSD-validatie en om berichten in het geheugen aan te passen. Beide zijn gratis en komen van PyPI. `schema-cache/` bevat de externe schema's (GML, O&M, ...) al; `fetch_schemas.py` is alleen nodig als een nieuwe versie andere externe schema's gebruikt.

## Draaien

Dubbelklik `run_alle_versies.bat` (alle versies) of `versies/<versie>/run_tests.bat` (één versie), of vanuit `SLD testsuite`:

```
python run_tests.py                                                 alle versies (~15 s per versie, parallel)
python run_tests.py --versie "SLD_Extern_Uitwisselberichten v15.0"  alleen deze versie (mag vaker)
python run_tests.py --snel                                          zonder automatische controles
python run_tests.py --robuust                                       ook: XSLT loopt nooit vast op een herhaald element (~2 min per versie)
python run_tests.py -k Dossier                                      alleen tests met 'Dossier' in de naam
python run_tests.py --versie V --xslt-dir MAP                       XSLT's uit MAP testen (bijv. een aangepaste kopie)
python run_tests.py --update-baseline                               huidige uitvoer + controlelijst vastleggen als nieuwe baseline
python run_tests.py --workers 4                                     aantal parallelle processen (standaard: cores - 1, max 16)
```

De opties van `run_tests.bat` worden doorgegeven, bijv. `run_tests.bat -k Dossier`. Na elke run staat er per versie een rapport in `versies/<versie>/report/report.html` (met filter "alleen gefaalde tests"); bij meerdere versies volgt in de terminal een overzicht. Exitcode 0 = niets gefaald, 1 = iets gefaald.

**Tip bij het aanpassen van een XSLT:** werk in een kopie en test die eerst met `--versie ... --xslt-dir`, of draai de tests direct na je wijziging en kijk in het rapport.

## Wat wordt er getest (per versie)

| Groep | Wat |
|---|---|
| XSLT's | Alle vier XSLT's compileren, lookupbestanden zijn well-formed, en de meetversie (zie onder) geeft exact dezelfde meldingen als het origineel. |
| XSD-validatie | Alle inname-voorbeelden valideren tegen `issld-messages.xsd`, alle uitgifte-voorbeelden tegen `dssld-messages.xsd`. Uitgifteberichten zitten in een SOAP-envelop; daarvan wordt de inhoud van `soap:Body` gevalideerd. |
| Voorbeeldberichten | Elk officieel innamebericht gaat door de XSLT die erbij hoort (zie tabel hierboven) en moet 0 ERRORs geven. |
| Testberichten | Afgeleide berichten in `versies/<versie>/testberichten/` (zie onder), ook 0 ERRORs (of bekende afwijking). |
| Baseline | De volledige uitvoer per bericht moet exact gelijk zijn aan `versies/<versie>/baseline/` (volgorde maakt niet uit). Bij verschil zie je welke meldingen erbij kwamen of verdwenen. |
| Controlelijst | Alle controle-aanroepen in elke XSLT (met parameters, zoals ERROR/WARNING) moeten gelijk zijn aan `versies/<versie>/baseline/controlelijst *.json`. Vangt een weggehaalde of gewijzigde controle. |
| Automatische controles | Voor elke standaard-controle (checkExistence, checkFilled, checkLookupId, checkLength, checkExactLength, datums, geometrie, coördinaten) wordt een element in een bericht bewust fout gemaakt; de test slaagt alleen als precies díe controle een melding geeft. Nieuwe controles gaan automatisch mee. |
| Testcases | Handgeschreven cases uit de gedeelde `cases.json` voor de overige controles (aantallen objecten, koppeling met besluiten, dossier-id's, Nature, lokaalId, eenheid bij Depth, ...). |
| Robuustheid (alleen met `--robuust`) | In elk bericht wordt elk element binnen de SIKB-inhoud één voor één gedupliceerd; de XSLT mag daarbij nooit vastlopen met een runtime-fout (bijv. `string()` of `lower-case()` op twee waarden). Draai dit na een grotere XSLT-wijziging. |

Loopt een XSLT bij een (aangepast) bericht vast met een runtime-fout, dan wordt die test FAIL met de foutmelding erbij; de rest van de run gaat door.

**Dekking**: onderaan het rapport staat per XSLT hoeveel controles in minstens één test een melding gaven, de lijst die nog nooit geraakt is, en de controles die als onbereikbaar zijn uitgesloten. Alleen een volledige run (zonder `-k`/`--snel`) geeft een representatieve dekking.

### Hoe weet de test welke controle een melding gaf?
De runner maakt in het geheugen een *meetversie* van elke XSLT waarin elke controle-aanroep zijn regelnummer aan de melding meegeeft, en een *verkenningsversie* die registreert welke elementen welke controle bereiken. De originele XSLT wordt niet aangepast; een aparte test bewaakt dat de meetversie exact dezelfde meldingen geeft.

## Bestanden

**Gedeeld (`SLD testsuite/`)**

| Bestand | Doel |
|---|---|
| `run_tests.py`, `run_alle_versies.bat` | De testrunner. |
| `suite.json` | SLD-instellingen: mapnamen binnen een versie, XSD-namen, welke berichtsoort/kwaliteit naar welke XSLT, extra namespaces. |
| `xslt_sites.py` | Vindt de controle-aanroepen in de XSLT en maakt de meet- en verkenningsversie. |
| `cases.json` | Handgeschreven testcases voor alle versies. |
| `nieuwe_versie.py` | Zet `versies/<nieuwe versie>/` klaar voor een nieuwe versie (zie *Versies wisselen*). |
| `maak_testberichten.py` | Maakt `versies/<versie>/testberichten/` opnieuw aan uit de officiële voorbeelden (alle versies, of één: `python maak_testberichten.py "SLD_Extern_Uitwisselberichten v15.0"`). |
| `fetch_schemas.py`, `schema-cache/` | Externe schema's voor de XSD-validatie. |

**Per versie (`versies/<naam van de geleverde map>/`)**

| Bestand | Doel |
|---|---|
| `run_tests.bat` | Test alleen deze versie. |
| `versie.json` | Waarden die per versie verschillen, gebruikt als `${NAAM}` in `cases.json` (nu nog leeg). |
| `overrides.json` | Aanpassingen op automatische controles (overslaan, andere mutatie), altijd met reden. |
| `bekende_afwijkingen.json` | Bewust geaccepteerde afwijkingen (status BEKEND i.p.v. FAIL). |
| `onbereikbaar.json` | Controles die nooit kunnen afgaan (dode code), met reden; tellen niet mee in de dekking. |
| `baseline/` | Vastgelegde uitvoer per bericht + controlelijst per XSLT. |
| `testberichten/`, `report/` | Afgeleide testberichten en het rapport. |

### Testberichten
Sommige controles worden door geen enkel voorbeeldbericht bereikt. `maak_testberichten.py` leidt daarom drie extra berichten af:

| Testbericht | Waarom |
|---|---|
| T1. New Decision met Project en endTime (van 03c_2) | Geen New Decision-voorbeeld heeft een Project (type 11) of een `endTime` bij Remediation/ContaminationInformation. |
| T2. Change SoilLocation met naam (van 03b) | De SoilLocation in 03b heeft geen `name`. |
| T3. WBB Complete Report met Dossier-broId (van 02) | Geen Complete/Start Report-voorbeeld heeft een `broId` bij het Dossier. |

## Een testcase toevoegen

Voeg een blok toe aan `SLD testsuite/cases.json`; de case draait dan in alle versies:

```json
{
  "name": "Bestand - twee Dossiers",
  "sources": ["02_registrationRequest_SLD_CompleteReport_IMBROA_WBB.xml",
              "03b_registrationRequest_SLD_ChangeSoilLocation_IMBROA_WBB.xml"],
  "mutations": [
    { "xpath": "//imsikb0101:featureMember[imsikb0101:Dossier]", "action": "duplicate" }
  ],
  "expect": { "type": "ERROR", "title_contains": "xml-bestand", "message_contains": "maximaal 1 Dossier" }
}
```

- `source` (één bericht) of `sources` (lijst; de case draait per bericht). Welke XSLT gebruikt wordt, volgt uit het bericht (zie tabel). Voorbeeld- én testberichten mogen. Handige keuzes: `01_registrationRequest…_IMBRO_OW.xml` (OW), `02_registrationRequest…_IMBROA_WBB.xml` (WBB Complete Report), `03b_…ChangeSoilLocation…` en `03c_…NewDecision…_2.xml`.
- `action`: `remove`, `set` (tekst → `value`), `set_attribute` (`name` + `value`), `duplicate`, `insert_xml` (`xml`; standaard als laatste kind, met `"position": "after"` erna). Met `"first_only": true` alleen het eerste gevonden element.
- `expect` mag een lijst zijn (ook leeg); `not_expect` = meldingen die juist níet mogen verschijnen; `waarom` = toelichting in het rapport.
- De verwachte melding moet *nieuw* zijn t.o.v. het onbewerkte bericht.
- Prefixen in XPath: `imsikb0101`, `immetingen`, `gml`, `om`, `sam`, `sams`, `spec`, `xlink`, `xsi`, `issld`, `sldcom`.
- Let op: een `Decision` staat bij SLD binnen het Dossier (`//imsikb0101:Dossier/imsikb0101:decisions/imsikb0101:Decision`), niet direct onder een `featureMember`.

**Verschillen tussen versies:**
- Een waarde die per versie verschilt schrijf je als `${NAAM}` en zet je in elke `versie.json` onder `variabelen`.
- Een case die maar voor één versie geldt krijgt `"versies": ["SLD_Extern_Uitwisselberichten v15.0"]` (de mapnaam).

## Werkwijze bij veelvoorkomende wijzigingen

### Ik pas een voorbeeldbericht aan
De tests lezen de voorbeeldberichten bij elke run opnieuw in; automatische controles en testcases gebruiken dus direct de nieuwe inhoud. Wat je daarna doet:

1. Draai de tests voor die versie: `run_tests.bat` in `versies/<versie>` (of `python run_tests.py --versie "<versie>"`).
2. Waarschijnlijk faalt de groep **Baseline** voor dat bericht: het rapport toont precies welke meldingen erbij kwamen of verdwenen. Is dat wat je verwachtte? Leg het vast:
   ```
   python run_tests.py --versie "<versie>" --update-baseline
   ```
3. Het bericht moet nog steeds **0 ERRORs** geven (groep *Voorbeeldberichten*). Bevat het bewust een fout, zet dat dan in `bekende_afwijkingen.json` van die versie.
4. Heb je een element verwijderd of een `gml:id` veranderd waar een testcase naar verwijst, dan faalt die case met *"XPath vond geen element"*. Pas de XPath in `cases.json` aan (of kies een ander bronbericht).
5. Zijn T1–T3 van dit bericht afgeleid (03c_2, 03b, 02), maak ze dan opnieuw: `python maak_testberichten.py "<versie>"`, en draai stap 2 opnieuw.
6. Een **nieuw** voorbeeldbericht in de innamemap wordt automatisch meegenomen (als het bij een regel in `suite.json` past); de eerste run maakt er een baseline voor aan.

### Ik breid een XSLT uit met een nieuwe controle
1. Pas de XSLT aan en draai de tests voor die versie.
2. De groep **Controlelijst** faalt met *"+ nieuw: sikb:…"*. Dat is de bevestiging dat de runner je nieuwe controle ziet.
3. Kijk wat voor controle het is:
   - **Een standaardfunctie met `.` als context** (`checkExistence`, `checkFilled`, `checkLookupId`, `checkLength`, `checkExactLength`, `checkDateBeforeDate`/`AfterDate`, `checkGeometryElement(s)`, `checkCoordinates`): die wordt **automatisch getest**. Niets te doen, tenzij hij als *NIET TESTBAAR* verschijnt: dan heeft geen enkel voorbeeld- of testbericht het betreffende element. Voeg dan een testcase toe die het element met `insert_xml` toevoegt, of breid `maak_testberichten.py` uit.
   - **Een eigen melding (`sikb:createRecord`) of een functie met een andere context** (bijv. `$variabele` of `./iets`): die verschijnt bij **Dekking → niet geraakt: regel …**. Schrijf daarvoor een testcase in `cases.json`:
     1. zoek in de XSLT onder welke voorwaarde de melding ontstaat;
     2. kies voorbeeldberichten van alle XSLT's waar de controle in staat (via `sources`);
     3. beschrijf met `mutations` hoe je het bericht fout maakt, en met `expect` een stukje van de verwachte `Title`/`Message`;
     4. probeer de case los uit: `python run_tests.py --versie "<versie>" --snel -k "<naam van je case>"`.
   - Let op: ook als de dekking al 100% zegt, kan een nieuwe `createRecord` "toevallig" geraakt zijn door een andere test. Voeg er toch een case voor toe.
4. Alles zoals verwacht? Leg de controlelijst vast: `python run_tests.py --versie "<versie>" --update-baseline`.
5. Draai tot slot een volledige run en controleer dat de dekking weer 100% is.
6. Geldt de nieuwe controle maar voor één versie? Geef de case dan `"versies": ["<versie-map>"]`.

### Ik verander een meldingstekst of ERROR ↔ WARNING
De groepen **Baseline** (als een voorbeeldbericht die melding geeft), **Controlelijst** en de testcases met `message_contains`/`type` op die melding falen. Controleer in het rapport dat alleen verandert wat je bedoelde, pas de betreffende cases in `cases.json` aan en draai `--update-baseline`.

### Ik repareer een controle die in `onbereikbaar.json` staat
Haal hem uit `onbereikbaar.json` van die versie (en de bijbehorende `skip` in `overrides.json`, als die er is), draai de tests (de controlelijst meldt de gewijzigde aanroep) en daarna `--update-baseline`. Is het een standaardfunctie met `.` als context geworden, dan wordt hij automatisch getest; anders een testcase toevoegen.

## Wanneer `--update-baseline`?
Alleen als je een verandering **bewust** hebt gemaakt: een meldingstekst aangepast, een controle toegevoegd/verwijderd, of ERROR ↔ WARNING gewijzigd. Kijk eerst in het rapport (groepen *Baseline* en *Controlelijst*) wat er verandert. Combineer met `--versie` om alleen de baseline van die versie bij te werken.

## Versies wisselen (bijv. 15.1 erbij, 14.9.0 vervalt)

### Nieuwe versie toevoegen
1. **Map neerzetten** – zet de geleverde map (bijv. `SLD_Extern_Uitwisselberichten v15.1`, met `Controle XSLT/`, `Voorbeeldberichten/` en `XSD/`) naast de andere versies. Verder niets aan toevoegen. Een run meldt nu: *"heeft nog geen testconfiguratie"*.
2. **Tests klaarzetten** – vanuit `SLD testsuite`:
   ```
   python nieuwe_versie.py "SLD_Extern_Uitwisselberichten v15.1" --van "SLD_Extern_Uitwisselberichten v15.0"
   ```
   Dit maakt `versies/SLD_Extern_Uitwisselberichten v15.1/`, kopieert de instellingen van de meest verwante versie, toont welke XSLT's/XSD's/lookups verschillen, haalt eventuele nieuwe externe schema's op en maakt de testberichten. Baseline en rapport worden bewust níet gekopieerd.
3. **`versie.json` nalopen** – ontbreekt er een variabele, dan faalt de betreffende case met een duidelijke melding.
4. **Eerste run** – `python run_tests.py --versie "SLD_Extern_Uitwisselberichten v15.1"`. Deze run legt de baseline en controlelijst vast; beoordeel daarna elke FAIL.
5. Kijk naar de **dekking** in het rapport.

### Versie laten vervallen
1. Haal de geleverde map weg (verplaats naar een archief of verwijder) **en** verwijder of archiveer `SLD testsuite/versies/<die map>/`. Alleen tijdelijk uitzetten? Verplaats dan alleen `versies/<die map>` naar bijv. `SLD testsuite/versies (uit)/`.
2. Ruim in `cases.json` eventueel cases met `"versies": ["<vervallen map>"]` op.
3. Draai `run_alle_versies.bat` ter controle.

## Bevindingen in de SLD-XSLT's en reparaties (11-11-2026)

Bij het opzetten van de tests zijn drie problemen gevonden. Ze zijn in alle vier XSLT's van beide versies gerepareerd (de kopregel/datum van de XSLT's is niet aangepast):

| Bevinding | Reparatie | Getest door |
|---|---|---|
| Bij WBB (Complete/Start Report en New Decision) werd een Project alleen gecontroleerd als `projectType` "id:11" bevatte. Een Project zónder projectType werd stilletjes overgeslagen, en `contains(…, 'id:11')` accepteerde ook bijv. id:110. | Een gekoppeld Project wordt nu ook gecontroleerd als `projectType` ontbreekt of leeg is (zodat de verplichting gemeld wordt). Met projectType wordt alleen **exact** id 11 geaccepteerd; type 44 wordt, zoals bedoeld, nog steeds overgeslagen. | automatische controles + cases "WBB - Project …" |
| `sikb:checkLookupId(./value, 'immetingen:Depth', '@uom', 'Eenheid', 'ERROR')` was dode code: de eenheid van een diepte werd nooit gecontroleerd. | Vervangen door een eigen controle: `@uom` van `immetingen:value` moet een code uit de Eenheid-tabel van de lookup zijn, anders een ERROR. Bewust **geen** controle op de BRO-SLD-vlag: die staat voor alle 346 eenheden op false. | cases "Depth - …" |
| Een herhaald element (bijv. twee keer `dossierIdLocalAuthority`, een dubbel `version`, of twee geometrie-elementen) liet de XSLT vastlopen met een runtime-fout in plaats van een melding. | De hulpfuncties en de root-/featureMember-/geometrie-expressies gebruiken nu het eerste voorkomen (`(...)[1]`); `checkFilled` meldt het als één van de voorkomens leeg is. Daarna liepen 0 van de ruim 2.300 duplicaties per versie nog vast. | cases "Dossier - dubbel …" + groep *Robuustheid* (`--robuust`) |

`onbereikbaar.json` is daardoor nu leeg voor beide versies.
