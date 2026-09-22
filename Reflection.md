## Reflektion

### Vilka var de viktigaste problemen i originalkoden?

Ett av de viktigaste problemen var att koden saknade en `main()`-funktion.
 Det gjorde att hela programmet kördes när vi försökte importera en funktion, till exempel `summarize_by`, för att testa den. Det blev därför svårt att testa olika delar av programmet separat. Vi löste detta genom att lägga huvudkoden i en `main()`-funktion och använda `if __name__ == "__main__":`. På så sätt körs programmet bara när filen startas direkt, och funktionerna kan importeras och testas separat.

Ett annat problem var att koden använde `raise Exception("Fel data")` när en obligatorisk kolumn saknades. Felmeddelandet visade inte vilken kolumn som saknades, vilket gjorde det svårare att hitta och rätta felet. Vi ändrade detta så att programmet visar exakt vilka kolumner som saknas.

Ett tredje problem var att koden för `sales_by_category`, `sales_by_region` och `returns_by_category` innehöll mycket liknande kod. Samma typ av `groupby`, beräkningar, avrundning och sortering användes på flera ställen. Det gjorde koden längre och ökade risken för att en ändring missades på något ställe. Det kunde till exempel leda till att `return_rate` visades som procent i vissa rapporter men som decimaltal i en annan rapport. Vi löste detta genom att skapa en gemensam funktion, `summarize_by`, som kan användas för de olika sammanställningarna.


### Vilka förändringar tycker du förbättrade programmet mest?

Alla ändringar var viktiga, men de som gjorde störst skillnad var förbättringen av felmeddelandet (att visa exakt vilka kolumner som saknas, istället för ett generellt fel) och skapandet av `main()`-funktionen, som gjorde det möjligt att testa varje del av programmet separat.




### Varför valde du den projektstruktur du använde?

Jag valde att dela upp koden i tre filer utifrån vad varje del av programmet ansvarar för. `config.py` innehåller inställningarna och `ReportConfig`. `transform.py` innehåller funktionerna `summarize_by` och `validate_columns`, som arbetar med datan utan att behöva veta var filen kommer ifrån eller var resultatet ska sparas. `main.py` innehåller programmets huvudflöde, där vi läser in filen, använder funktionerna och sparar resultatet.

Jag valde den här strukturen eftersom den gör koden enklare att förstå och testa. Till exempel kan vi testa funktionerna i `transform.py` separat utan att behöva läsa in en fil eller köra hela programmet.



### Var använde du OOP/dataclass och varför passade det där?

Jag använde `dataclass` i `config.py` för klassen `ReportConfig`. Den används för att samla programmets inställningar, till exempel `input_path` och `output_dir`.

Jag valde `dataclass` eftersom det gör koden enklare och tydligare. Jag använde också `frozen=True`, vilket gör att inställningarna inte kan ändras av misstag när programmet körs. `kw_only=True` gör att vi måste skriva namnen på argumenten när vi skapar `ReportConfig`, vilket minskar risken att blanda ihop input- och outputsökvägen.

Med `dataclass` slipper vi också skriva mycket kod själva, till exempel en egen `__init__`-funktion.


### Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?

Mina tester kontrollerar att beräkningarna av `total_sales` och `return_rate` fungerar korrekt för både kategori och region. De testar också att `validate_columns` ger ett fel om en obligatorisk kolumn saknas.

Om någon ändrar `summarize_by` i framtiden och råkar skapa ett fel, kommer `pytest` att visa vilket test som inte längre fungerar. På så sätt kan vi upptäcka felet direkt istället för att det senare leder till felaktiga rapporter.


