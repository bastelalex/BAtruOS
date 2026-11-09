# Meilensteine und gasfreie Abnahme

| Gate | Ergebnis | Konkrete Abnahme |
| --- | --- | --- |
| M0 | Entwurf / Simulation | Hosttests grün, Demo eindeutig markiert, keine Originalpin-Verbindungen |
| M1 | Rekonstruktion | Revision identifiziert, beidseitige Fotos mit Maßstab, jede Netzzuordnung mit Quelle, unabhängiger Review; offene Knoten gesperrt |
| M2 | Messfrontend | Bereiche/Lastbudget belegt, Schutz/Isolation gerechnet, Rückspeisung bei Hub aus gemessen, ERC/DRC und Review abgeschlossen |
| M3 | Gasfreier Prüfstand | kein Gas, kein Zünder/Gasventil; strombegrenzte Versorgung, dokumentierte abgesicherte Ersatzlasten; Fehlerfälle und Sollwerte vor Test festgelegt |
| M4 | Integrierte Diagnose | 60 min synthetische/Prüfstandsdaten ohne ungemeldeten Verlust, Zeitstempel monoton, CSV/JSON vergleichbar, CYD DEMO/STALE/FAULT sichtbar; Neustart, Linkverlust und Queue-Überlauf geprüft |
| M5 | Montagehilfe / Kits | Placement-Ursprung und Bohrungen verifiziert, Maßprobe vor Druck, Kollisionen/Entnahme geprüft, FixKit-Prüfnachweise und Ready2Löt-BOM vollständig |

Pro Test: Aufbauplan, Geräte, Revisionen, Ersatzlastdimensionierung, Soll/Ist, Rohdaten, Datum/Prüfer und Abweichungen ablegen. Nicht bestandene Gates sperren Folgeschritte. M0 ist softwareseitig prüfbar; Hardwaregates sind offen. Kein Gate hier erteilt Freigabe für Gasbetrieb oder Produktlinie X.
