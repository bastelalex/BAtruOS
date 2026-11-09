# RetroControl H1 – technischer Start

Status: Entwurf und synthetischer Prototyp. Keine betriebsfähige Ersatzsteuerung.
Die originale E1800-Sicherheitssteuerung bleibt erhalten. Keine Gasventil-/Zündansteuerung und keine Überbrückung von Schutzfunktionen. X ist ein späterer separater Zweig mit eigenem Sicherheitskonzept und regulatorischer Freigabe; ein DevKit-Label ersetzt diese nicht.

## Struktur und Einstieg

- `docs/`: [Rekonstruktion](docs/e1800-reverse-engineering.md), [Architektur](docs/architecture.md), [Abnahme](docs/milestones.md).
- `hardware/`: KiCad-Modulplanung und getrennte Kit-Stücklisten; noch keine Fertigungsfreigabe.
- `firmware/`: portabler C++17-Diagnosekern und ESP32/CYD-Portierungsplan.
- `mechanical/`: Placement-Importer und parametrischer OpenSCAD-Entwurf.
- `assembly/`: Montagefolge und QR-Vertrag.
- `tests/`: gasfreie Host- und Datenformatprüfungen.

Ab Repository-Wurzel: `python3 -m unittest discover -s retrocontrol/tests -v`.
Demo: `g++ -std=c++17 -Wall -Wextra -Werror retrocontrol/firmware/sim.cpp -o /tmp/retrocontrol-sim && /tmp/retrocontrol-sim`.
Mechanik: `python3 retrocontrol/mechanical/placement.py retrocontrol/mechanical/placement.example.csv /tmp/placement.scad`;
mit OpenSCAD: `openscad -I /tmp -o /tmp/assistant.stl retrocontrol/mechanical/assistant.scad`.
Beispielkoordinaten sind fiktive RC-MAIN-Daten, keine E1800-Geometrie.
