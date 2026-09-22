# Orderrapport
Ett Python-program som läser orderdata från en CSV-fil och skapar rapporter över försäljning, returer och statistik per produktkategori och region.


## Installation
1. Klona repot
2. Skapa en virtuell miljö: `python -m venv .venv`
3. Aktivera den: `source .venv/Scripts/activate` (Windows/Git Bash)
4. Installera beroenden: `pip install -r requirements.txt`


## Användning
Kör programmet:
```bash
python -m src.order_report.main
```

## Tester

Kör testerna:
```bash
pytest
```




## Projektstruktur

```
order_report_project/
├── src/
│   └── order_report/
│       ├── __init__.py
│       ├── config.py       # ReportConfig (dataclass)
│       ├── transform.py    # summarize_by, validate_columns
│       └── main.py         # Programmets startpunkt
├── tests/
│   └── test_summarize_by.py
├── data/
│   └── orders.csv
├── output/
├── requirements.txt
├── pyproject.toml
├── code_review.md
└── README.md
```