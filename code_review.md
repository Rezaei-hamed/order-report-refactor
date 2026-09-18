# Kodgranskning av order_report.py

## Granskningsfynd

### Fynd 1 – Otydligt felmeddelande när kolumner saknas

**Observation:** Den gamla koden använde `raise Exception("Fel data")` när en obligatorisk kolumn saknades. Den visade inte vilken kolumn som saknades.

**Konsekvens:** Det blev svårt att förstå vad som var fel och vilken del av datan som behövde ändras.

**Förslag:** Använd `ValueError` och visa namnet på de kolumner som saknas i felmeddelandet. Då blir det lättare att hitta och rätta felet.

### Fynd 2 – Samma kod upprepas flera gånger

**Observation:** Koden för `sales_by_category` och `sales_by_region` är nästan likadan. Den använder samma `groupby`, beräkningar, avrundning och sortering. Det enda som ändras är vilken kolumn man grupperar efter.

**Konsekvens:** Om vi behöver ändra något i beräkningen måste vi ändra koden på flera ställen. Det finns då risk att man glömmer ett ställe.

**Förslag:** Skapa en gemensam funktion, till exempel `summarize_by(data, group_column)`, som kan användas för både kategori och region. Då behöver vi inte skriva samma kod flera gånger.

Fynd 3 – print() användes för all utskrift

Observation: Koden använde print() både för vanlig information, till exempel hur många rader som lästes in, och för felmeddelanden.

Konsekvens: Det blev svårt att skilja mellan vanlig information och fel. Det gick också inte att styra vilka meddelanden som skulle visas.

Förslag: Använd Pythons logging-modul. Använd logger.info() för vanlig information och logger.error() för fel. Logging kan sedan konfigureras centralt med logging.basicConfig().