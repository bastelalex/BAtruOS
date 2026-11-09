# H1: VampireKit und Diagnosearchitektur

## Datenweg

Originalplatine → passiver Clip/Federhaken → geschütztes, ggf. isoliertes Messfrontend → externer ADC bzw. Flankenerfassung → ESP32-WROOM-32E → Logging / CYD-UI.
Passiver Abgriff bedeutet ohne aktive Einspeisung; die Messkette benötigt eigene Versorgung. Rückspeisung auch bei ausgeschaltetem Hub untersuchen. Originale Schutzfunktionen bleiben autonom.

| Modul | Verantwortung | Freigabeabhängigkeit |
| --- | --- | --- |
| RC-MAIN | ESP32-WROOM-32E, Versorgung, externer ADC, Logging, UI-Link | Frontend- und Versorgungskonzept |
| RC-VAMP8 | modularer 8-Kanal-Abgriff via IC8-Clip/Federhaken | IC8-Gehäuse und Knotenmessungen |
| RC-DIG8 | getrennte geschützte Flanken-/Zeitmessung | Pegel, Bandbreite, Isolation |
| RC-TEST | Signalgeneratoranschluss, Ersatzlasten, Testpunkte | nur gasfreier Prüfstand |
| RC-E1800 | revisionsgebundener Zwischenadapter | vollständige Pinout-Prüfung, gesperrt |

## Messanforderungen (Entwurfsziele)

Acht langsame Kanäle, Ziel 10 Samples/s je Kanal, externe ADC-Erfassung mit Zeitstempel und Kalibrierdaten. Frontend-Eingangswiderstand vorläufig >=1 MΩ; endgültige Lastgrenze aus Quellenimpedanz und zulässiger Messabweichung ableiten. Auflösung, Eingangsspannung, Gleichtaktbereich und Schutzgrenzen sind offen. Keine ADC-Auswahl vor Bestimmung dieser Werte.
Acht schnelle Kanäle als Ausbauziel: separate Komparator-/Capture-Kette statt Polling des langsamen ADC. Maximale Frequenz, Pulsbreite, Totzeit und Pegel vor Auswahl von Capture-Hardware/Isolation messen. Überlauf und Datenverlust ausdrücklich melden.
Pro Eingang Testpunkte vor/nach Schutz, definierter Bezug, dokumentierte Clamp-Ströme, Eingangsimpedanz und Rückspeisung. Dimensionierung von Serienwiderständen, Filtern, Überspannungsschutz und Isolation erst nach E004–E006. Keine Originalpins in diesem Entwurf.

## ESP32 und CYD

Hub und 2,8-Zoll-CYD sind getrennte Geräte (CYD besitzt üblicherweise eigenen Controller; konkrete Variante prüfen). UI-Link zunächst UART als logischer Vertrag; Pins, Pegel und galvanischer Bezug bleiben bis zur Boardprüfung offen. Nachrichten: versioniertes JSON mit Sequenz, Zeitstempel, Quelle `synthetic`/`measured`, Kanal und Qualität. CYD darf keine Aktoren kommandieren. Disconnect/Timeout zeigt STALE; synthetische Werte werden dauerhaft als DEMO markiert.

Tasks: Acquisition → begrenzte Queue → Logger und UI-Publisher; Queue-Überlauf zählt verlorene Frames. Monotone Zeit im Hub, UTC nur zusätzlich nach Synchronisation. CSV/JSON haben dieselben Felder; reale Messwerte bleiben ungültig bis Kalibrierung und Freigabe. Speicherung und Transport dürfen Erfassung nicht blockieren.

## Zustände und Fehlersuche

`BOOT → DEMO` im aktuellen Prototyp. Geplant: `BOOT → SELF_TEST → OBSERVE`; von dort bei Timeout `STALE`, bei Frontend-/Pufferfehler `FAULT`. Rückkehr nur nach erneutem Selbsttest. Das sind Diagnosezustände, keine behaupteten Brennerzustände. Fehlerbericht enthält Modul, Kanal, Revision, Rohdaten und Qualität; keine automatische Reparatur oder Schutzüberbrückung.
