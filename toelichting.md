[h2 is vereist vanwege ReSpec]: #
<h2>Overheidsbesluit bodemverontreiniging</h2>

# Inleiding
De catalogus voor het overheidsbesluit bodemverontreiniging beschrijft de gegevens die in de registratie ondergrond zijn opgenomen van een gebied waarin bodemverontreiniging is geconstateerd en/of aangepakt vanuit het vakgebied milieukwaliteit.

Binnen de ontwikkelperiode van deze catalogus heeft er een wijziging plaatsgevonden in de wet- en regelgeving voor de aanpak van bodemverontreiniging. Vanaf 1 januari 2024 is de Omgevingswet (Ow) in werking getreden. Deze vervangt de Wet bodembescherming (Wbb). Een deel van de registratie van bodemverontreinigingen is in de zogenaamde ‘warme overdracht’ overgedragen naar een nieuw bevoegd gezag (doorgaans van provincie naar een gemeente). Een deel van deze registratie heeft geen vervolg meer of er geld overgangsbeleid onder het regime van de Wbb. En vanaf 1 januari 2024 is nieuwe informatie geregistreerd onder het regime van de Ow. We herkennen drie mogelijke categorieën van type dossiers die binnen SLD mogelijk moeten zijn, deze zijn in onderstaande figuur beschreven. Bij het opstellen van de catalogus is rekening gehouden met deze 3 categorieën.

Deze drie categorieën vertalen zich als volgt naar de afwegingen die in het model zijn gemaakt:
- __Kader aanlevering Wbb of Ow:__ regime waaronder de gegevens zijn aangemaakt is bepalend. Categorie 1 en 2 vallen onder Kader aanlevering Wbb, Categorie 3 valt onder Ow
- __Eenmalige aanlevering of aanvulling mogelijk:__ In de meeste situatie gaat het om eenmalige aanlevering. Categorie 1 locaties zijn afgerond onder Wbb en worden als digitaal archief aangeleverd. Categorie 3 locaties betreft de evaluatie achteraf van de uitgevoerde sanering of grootschalig graven >I-waarde. Onder de Ow wordn gegevens eemalig aangeleverd. Uitzondering zijn lopende Wbb gevallen die onder overgangsrecht doorgaan. Daarop kunnen aanvullingen komen. Bijvoorbeeld omdat een sanering is uitgevoerd en bevoegd gezag moet instemmen met uitgevoerde sanering of nazorgplan. 
- __IMBRO/A of IMBRO:__ De eisen die worden gesteld onder IMBRO kunnen strenger zijn dan onder IMBRO/A (bijvoorbeeld omdat meer velden verplicht gevuld moeten zijn onder IMBRO). Voor gegevens waarbij eenmalige aanlevering geldt is de keuze om dit te doen onder IMBRO/A voor gegevens ontstaan voor 1-1-2025 (in werking treden BRO Milieukwaliteit). Dat betreft categorie 1 en een deel van categorie 3. De eerste aanlevering van gegevens in categorie 2 kan ook onder IMBRO/A (betreft vooral archiefaanlevering). Aanvullingen op categorie 2 kunnen zowel onder IMBRO als ondr IMBRO/A worden gedaan. Nieuw ontstane gegevens in categorie 3 worden onder IMBRO aangeleverd.

Het resultaat is weergeven in onderstaande figuur dat weergeeft hoe gegevens worden geregistreerd.

Een overheidsbesluit bodemverontreiniging bestaat uit de gegevens die bepalend zijn geweest in de procedure van bevoegd gezag bij de beoordeling en afhandeling van bodemverontreiniging. De locatie is vastgelegd in de contour van de bodemlocatie (regime Wbb) of het aangepakt gebied (regime Ow), waarbij onder het Wbb regime besluiten en extra contouren kunnen worden geregistreerd voor verontreinigingscontour of nazorgcontour.

# Belangrijkste entiteiten

## Registratieobject
Deze entiteit bevat een vijftal algemene gegevens van het registratieobject, die voor ieder registratieobject van toepassing zijn. Deze algemene gegevens hebben betrekking op het registratieobject zelf; de unieke identificatie (BRO-ID), de bronhouder, de dataleverancier en het van toepassing zijnde kwaliteitsregime (IMBRO/A of IMBRO) van aanlevering.

## Overheidsbesluit bodemverontreiniging
Deze entiteit bevat de gegevens die het registratieobject identificeren en inzicht geven in de totstandkoming en context van het object voorafgaand aan opname in de registratie ondergrond. Het kader aanlevering is daarbij bepalend voor de registratie.

De term voor het registratieobject Overheidsbesluit bodemverontreiniging is breder dan alleen het formele besluit dat door de overheid is genomen. Ook moet de term van ‘besluit’ breder worden opgevat: een overheidsbesluit bodemverontreiniging bestaat uit de gegevens die bepalend zijn geweest in de procedure van bevoegd gezag bij de beoordeling en afhandeling van bodemverontreiniging. Dit omvat de gegevens die onderdeel zijn van een formele beschikking, maar ook het besluit van de overheid om gegevens te registreren zonder dat er een formele beschikking bij hoort (zoals bijvoorbeeld onder het regime van de Ow).

Dit attribuut bevat twee zogenaamde gegevensgroepen; de Registratiegeschiedenis (BRO generiek) en de Gestandaardiseerde locatie (BRO generiek).

Dit attribuut bevat twee zogenaamde gegevensgroepen; de Registratiegeschiedenis (BRO generiek, zie paragraaf 4.2.3) en de Gestandaardiseerde locatie (BRO generiek, zie paragraaf 4.2.4).

## Registratiegeschiedenis
De registratiegeschiedenis van een overheidsbesluit bodemverontreiniging geeft de essentie van de geschiedenis van het object in de registratie ondergrond, de zgn. formele geschiedenis. De registratiegeschiedenis vertelt bijvoorbeeld wanneer een object is geregistreerd en of er na registratie correcties zijn doorgevoerd. Deze gegevensgroep wordt niet aangeleverd maar intern binnen de registratie ondergrond vastgelegd.

## Gestandaardiseerde locatie
Locaties die zijn ontstaan onder het regime van de Ow worden geregistreerd via aangepakt gebied (zie paragraaf 4.2.8). Overige locaties (voornamelijk ontstaan onder het regime van de Wbb) worden als bodemlocatie geregistreerd (zie paragraaf 4.2.5). De gestandaardiseerde locatie geeft alleen de geografische afbakening van de locatie.

De geometrie kan worden aangeleverd ten opzichte van twee referentiestelsels (RD en ETRS89). Binnen de basisregistratie ondergrond worden gegevens die aangeleverd zijn volgens RD volgens een gedefinieerde methodiek omgezet naar ETRS89. Deze bewerking vindt plaats binnen de BRO zodat aan de uitgiftekant altijd kan worden uitgeleverd in ETRS89 én het oorspronkelijk aangeleverde referentiestelsel. De gestandaardiseerde locatie wordt vastgelegd, evenals de methode waarop de transformatie is uitgevoerd. Deze gegevensgroep heeft geen invloed op de aanlevering.

## Keuze Bodemlocatie of Aangepakt gebied
Zoals aangegeven in paragraaf 4.1 kunnen gegevens onder twee verschillende kaders aangeleverd worden: Wbb of Ow. Registraties die ontstaan zijn onder het regime van de Wbb (ongeacht of de aanpak is afgerond of dat sprake is van overgangsrecht) worden als ‘Bodemlocatie’ opgenomen in de BRO SLD. Registraties die ontstaan zijn onder het regime van de Ow worden als ‘Aangepakt gebied’ in de BRO SLD opgenomen. Het kader aanlevering dat is ingevuld bepaalt de keuze, en de keuze heeft gevolgen voor de gegevens die in de BRO worden vastgelegd. Daarna kan registratie verder plaatsvinden langs de lijn van Bodemlocatie (zie [paragraaf (#Bodemlocatie)) of Aangepakt gebied (zie paragraaf 4.2.7(#Aangepakt-gebied)).

## Bodemlocatie
Deze entiteit beschrijft de eenheid (of aggregatie van kleinere eenheden) die als één geheel is aangepakt bij het onderzoek naar en de aanpak van bodemverontreiniging. De entiteit bevat een aantal algemene gegevens die betrekking hebben op het registratieobject zelf, zoals: de unieke identificatie (zowel binnen het Bodeminformatiesysteem als in de dossiers van het bevoegd gezag), de naam en ruimtelijke begrenzing van de locatie, en het van toepassing zijnde kader van aanlevering aan de BRO. Tevens bevat deze entiteit het zogenaamde ‘SIKB-ID’ (unieke SIKB0101 Identificatie in de vorm van een GUID) waaronder de bodemlocatie in de ketensystemen is vastgelegd .Daarnaast bevat de entiteit enkele gegevens die betrekking hebben op de afhandeling door bevoegd gezag zoals de vervolgactie Wbb.

## Aangepakt gebied
Deze entiteit bevat de gegevens van de uitgevoerde bodemsanering of graafwerkzaamheden (Ow: graven in meer dan 25m3 in grond boven Interventiewaarde). Het gebied wordt beschreven aan de hand van enkele unieke kenmerken zoal SIKB-ID, locatiecode BIS, contour en compartiment. Daarnaast worden enkele gegevens over de aanpak genoemd: begin- en einddiepte, type saneringsaanpak, einddatum van de werkzaamheden. Het is mogelijk om een als milieuhygiënisch bodemonderzoek (SAD) geregistreerd bomonderzoek (evaluatierapport) te koppelen aan deze entiteit.

## Verontreinigd gebied
Deze entiteit bevat de gegevens van de bodemverontreiniging zoals afgebakend met een verontreinigingscontour. De entiteit bevat onder meer een aantal gegevens om het gebied te identificeren (SIKB-ID) en die aangeven wat de aard en omvang van de verontreiniging is: overschreden toetsingswaarde, compartiment en dieptetraject. De datum waarop de verontreiniging is vastgesteld zowel als de datum waarop de verontreiniging niet meer aanwezig is, kunnen worden geregistreerd.

## Nazorggebied
Deze entiteit bevat de gegevens van de vastgestelde nazorg en eventuele beperkingen die na afloop van de sanering zijn opgelegd. Naast identificerende kenmerken (SIKB-ID en contour) is het mogelijk aan te geven hoe lang de nazorg van toepassing is en op welke datum deze inwerking is getreden. In de bijbehorende Nazorgmaatregel kan worden gespecificeerd welke gebruiksbeperking is opgelegd.

## Besluit
Deze entiteit bevat de gegevens van besluiten en beschikkingen zoals door het bevoegd gezag zijn vastgelegd. Dit zijn doorgaans besluiten die zijn genomen in het kader van de Wbb over de vaststelling en aanpak van de bodemverontreiniging.

Deze entiteit bevat de gegevens die het besluit identificeren (SIKB-ID en kenmerk van het besluit) en inzicht geven in het besluittype en de datum waarop het besluit bekend is gemaakt.

# INSPIRE
Het doel van de Europese kaderrichtlijn INSPIRE is het harmoniseren en openbaar maken van ruimtelijke gegevens van overheidsorganisaties ten behoeve van het milieubeleid. Het registratieobject overheidsbesluit bodemverontreiniging valt niet onder een bestaand INSPIRE-thema. Mogelijk zal hier op een later tijdstip invulling aan worden gegeven.
