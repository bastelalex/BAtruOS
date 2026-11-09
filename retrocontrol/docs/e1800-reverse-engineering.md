# E1800: Rekonstruktion und Evidenz

Referenz laut Issue: Trumatic E1800 12 V. Revision unbekannt. Die zwei im ursprünglichen Chat erwähnten Fotos sind hier nicht verfügbar. Es gibt daher noch keine belegte Originalverbindung, Bauteilidentifikation oder Netzliste.

## Erfassung

Originale unter `hardware/e1800/evidence/` revisionsweise ablegen: Ober-/Unterseite senkrecht und hochauflösend mit Maßstab, Typenschild, Stecker mit Blickrichtung, PCB-Maße und Bohrungen, lesbare Aufschriften. Pro Quelle ID, Dateiname, SHA256, Datum, Revision und Orientierung erfassen. Unterseite für Annotation spiegeln, Original unverändert aufbewahren. Eigene stabile Annotation-IDs verwenden; Bestückungsdruck separat übernehmen.

## Evidenzmatrix

| ID | Gegenstand / Zuordnung | Status | Quelle | Nächster Nachweis |
| --- | --- | --- | --- | --- |
| E001 | Platinenrevision / Gerätevariante | offen | Issue #1, keine Fotos | Typenschild und PCB-Aufdruck |
| E002 | IC8-Clip: Gehäuse, Pin 1, Versorgung, Funktion | offen | nur Anforderung IC8-Clip | Aufschrift, Datenblattrevision und spannungsfreie Verfolgung |
| E003 | Steckverbinder: Anzahl, Orientierung, Pinbelegung | offen | keine | Fotos und Durchgangsprotokoll |
| E004 | Massebezug, Isolation, Versorgungspotentiale | offen | keine | spannungsfreie Netzverfolgung, später qualifizierte Messung |
| E005 | Langsame Messknoten und Lastempfindlichkeit | offen | keine | Quellenimpedanz und zulässige Zusatzlast ermitteln |
| E006 | Schnelle Signale: Pegel, Frequenz, Transienten | offen | keine | geeignete isolierte Messung am gasfreien Prüfstand |

`belegt`: Quelle plus reproduzierbarer Nachweis; `vermutet`: nachvollziehbare Hypothese mit Quelle und Gegenprüfung; `offen`: kein ausreichender Nachweis. Status nie aus ähnlichen E1800-Revisionen übertragen.
Netze erhalten neutrale IDs N0001 usw.; kein Funktionsname ohne Evidenz. Jede Kante wird einzeln in `hardware/e1800/net-evidence.csv` geführt. Leere CSV bedeutet keine belegten Netze.

## Messprotokoll je Punkt

Erfassen: Revision, Knoten-ID, Foto-Koordinate, Referenzpotential, Gerät/Tastkopf und Kalibrierung, Stromversorgung/Stromlimit, Betriebszustand, Rohdaten, Messunsicherheit, beobachtete Belastung und Prüfer. Durchgang nur spannungsfrei. Erst Masse-/Isolationskonzept, Spannungsbereich und Energie bewerten, danach geeignete Messmittel auswählen. Keine direkte ESP32-Verbindung. Keine Messung an Zündhochspannung mit einem Logik-/ADC-Frontend.

Freigabe des RC-E1800-Zwischenadapters erst nach überprüfter Pin-für-Pin-Matrix einschließlich Blickrichtung, Gegenstecker, Kabel und Revision. Bis dahin bleibt er vollständig unverdrahtet.
