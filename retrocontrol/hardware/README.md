# KiCad-H1-Arbeitsplan

Aktuell Architektur, keine freigegebenen Schaltpläne/PCBs. Pro Modul später eigenes KiCad-Projekt unter `kicad/<Modul>/`, mit hierarchischen Blättern Versorgung, Schutz/Isolation, Messung, Schnittstellen und Testpunkten. RC-MAIN-Zielmaß vorläufig 100 × 80 mm; Bohrungen und Mechanik noch offen.

Reihenfolge: Messbereiche belegen → Frontend berechnen/reviewen → Schaltplan/Footprints → ERC → Layout → DRC → unabhängiger Review → Fertigungsexporte. RC-E1800 bleibt bis Pinout-Freigabe gesperrt. Keine Gerber aus Platzhaltern erzeugen.

Je Freigabe archivieren: KiCad-Version, Revision, Quellen, Schaltplan-PDF, ERC/DRC-Berichte (keine ungeklärten Fehler; Ausnahmen begründen), BOM mit MPN/Alternativen, Placement mit Ursprung/Seite/Einheit, Gerber/Drill, Testpunktliste und Prüfprotokoll. Die Placement-Datei wird vor STL-Export gegen Platinenumriss und Bohrungen geprüft.

`bom-fixkit.csv` und `bom-ready2loet.csv` sind getrennte Beschaffungsvorlagen, keine einkaufsfertigen Stücklisten. FixKit: Spenderherkunft, Sichtprüfung, Werte-/Leckstrom-/Funktionsprüfung dokumentieren; unklare oder beschädigte Teile aussortieren. Ready2Löt: nachvollziehbare Neuteile und Wareneingangsprüfung. Kritische Schutz-/Isolationsbauteile erst nach Designreview spezifizieren.
