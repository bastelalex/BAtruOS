# BAtruOS

**Modulare Diagnose für ältere Heizungssteuerungen. Erster Prüfstand: Trumatic E1800 (12 V).**

Wenn eine ältere Heizungssteuerung ausfällt, beginnt die Fehlersuche oft mit einer lückenhaften Dokumentation. BAtruOS entwickelt dafür einen Werkstatt-Workflow: Signale erfassen, Zustandswechsel nachvollziehen und Messungen so dokumentieren, dass eine zweite Werkstatt sie wiederholen kann.

[Technischer Prototyp](https://github.com/bastelalex/BAtruOS/pull/2) · [Entwicklungsauftrag](https://github.com/bastelalex/BAtruOS/issues/1) · [Bastelalex](https://github.com/bastelalex)

## Das erste Projekt: RetroControl H1

**VampireKit** ist der Entwurf für eine modulare, passive Diagnoseplattform. Vorgesehen sind hochohmige Messadapter, ein ESP32-Diagnosehub, ein 2,8-Zoll-CYD-Touchdisplay und Messprotokolle in CSV und JSON. Bei H1 bleibt die originale Sicherheitssteuerung vollständig zuständig. H1 beobachtet Signale. Gasventil, Zündung und Schutzfunktionen bleiben unter Kontrolle des Originalsystems.

| Entwicklungsstand | Was sich ansehen lässt |
| --- | --- |
| **Im Pull Request** | Evidenzmatrix für die Platinenrekonstruktion, Architekturentwurf, portabler C++17-Diagnosekern mit synthetischen Daten, Placement-Importer und parametrischer OpenSCAD-Entwurf für einen Lötassistenten. |
| **Als Nächstes** | Platinenrevision und Geometrie erfassen, Messpunkte und Signalbereiche belegen, danach Adapter und Messkette auf einem gasfreien Prüfstand erproben. |
| **Spätere Produktlinie X** | Vollständiger Steuerungsersatz als eigenständiges Vorhaben mit eigenem Sicherheits- und Freigabeprozess. |

Die [technische README des Prototyps](https://github.com/bastelalex/BAtruOS/blob/codex/issue-1-retrocontrol-h1/retrocontrol/README.md) enthält den Einstieg in Simulation, Tests und CAD. Der Entwicklungsstand ist ein **Softwareprototyp mit synthetischen Messdaten**. Die Erprobung an Originalhardware steht aus.

## Pilot und Geschäftshypothese

Der erste denkbare Einsatz ist die **Fehlersuche am Werkstatttisch**. Ein Pilot mit spezialisierten Reparaturbetrieben kann zeigen, wie schnell sich bekannte Fehler eingrenzen lassen, ob verschiedene Personen dieselben Messergebnisse erhalten und welcher Aufwand beim Einrichten entsteht.

Wenn dieser Ablauf trägt, lässt sich prüfen, welche Teile des Messsystems für weitere Platinenrevisionen und Geräteserien wiederverwendbar sind. Zwei Kit-Varianten sind vorgesehen: **FixKit** mit geprüften Spenderbauteilen und **Ready2Löt** mit Neuteilen.

**Für Investoren und Pilotpartner:** Gesucht ist der Austausch mit Werkstätten, Prüfpartnern und Hardware-Investoren, die den Weg vom Diagnoseprototyp zum messbaren Werkstattpilot mitgestalten möchten. [Über GitHub Kontakt aufnehmen](https://github.com/bastelalex/BAtruOS/issues/new).

## English summary

BAtruOS is developing a modular diagnostic workflow for legacy heater control boards, starting with the 12 V Trumatic E1800. The H1 prototype uses simulated data today. The next milestone is a gas-free bench validation with real hardware. We're interested in conversations with specialist repair shops, test partners and early-stage hardware investors.
