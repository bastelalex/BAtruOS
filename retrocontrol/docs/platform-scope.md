# Offene Heizungsplattform

## Ziel und Gerätematrix

BAtruOS soll Gas- und Dieselstandheizungen, Boiler und Elektroheizungen sowie Kombinationen verschiedener Energieträger integrieren können. Herstellerunabhängigkeit entsteht durch dokumentierte Geräteprofile und austauschbare Adapter. Eine universelle elektrische Beschaltung wird nicht vorausgesetzt.

| Geräteklasse | Energieträger | Stand |
| --- | --- | --- |
| Trumatic E1800 | Gas, 12-V-Steuerung laut Issue #1 | erstes Referenzprojekt, Rekonstruktion offen |
| Weitere Standheizungen | Gas / Diesel | geplant, noch keine Profile |
| Boiler / Warmwassergeräte | Gas / Diesel / elektrisch / kombiniert | geplant, noch keine Profile |
| Raum- und Zusatzheizungen | elektrisch | geplant, noch keine Profile |

## Schichten

1. Gemeinsamer Kern: Zeitstempel, Einheiten, Messqualität, Logging, Diagnoseereignisse, UI und Montage-Datenvertrag.
2. Geräteprofil: Hersteller, Modell, Platinenrevision, Firmwareversion, Geräteklasse, Energieträger, Quellen und Fähigkeiten.
3. Transport und Adapter: nur pro Gerät belegte analoge Abgriffe, digitale Busse oder dokumentierte Hersteller-Schnittstellen. Unbekannte Pins bleiben unverbunden.
4. UI: zeigt nur nachgewiesene Fähigkeiten. Nicht vorhandene Sensoren liefern `unsupported` statt erfundener Messwerte; veraltete Daten bleiben als solche erkennbar.

Profile werden später unter `hardware/devices/<manufacturer>/<model>/<revision>/` abgelegt. Das bestehende `hardware/e1800/` bleibt vorerst die Arbeitsablage des Referenzgeräts. Gemeinsamer Kern enthält keine E1800-Pinbelegungen und keine Annahmen über Brennerabläufe anderer Geräte.

## Profilvertrag (geplante Erweiterung)

Pflichtfelder: eindeutige `device_id`, Profilversion, Hersteller/Modell, Hardware-/Firmware-Revisionsbereich, Geräteklasse, Energieträger, Quellen mit Evidenzstatus, Adapterrevision, Potential-/Versorgungskonzept, Kanalliste mit Einheit und Qualität, unterstützte Fähigkeiten, Prüfprotokolle und Freigabestatus. Unbekannte Revisionen passen niemals automatisch auf ein vorhandenes Profil.

Fähigkeiten getrennt deklarieren: `observe`, `read_status`, `read_faults` und gegebenenfalls später `request_setpoint`. Default ist keine Fähigkeit; schreibende Funktionen sind im aktuellen H1-Scope nicht implementiert. Ein Profil ist keine Sicherheitsfreigabe. Der aktuelle Demo-Datenvertrag v1 bleibt unverändert; Geräte-ID und Profilversion sind vor Mehrgerätebetrieb in einem versionierten Folgeformat zu ergänzen und zu testen.

## Unterstützungsstufen

`planned` → `documented` → `bench_verified` → `released_observation`.
Die Stufe gilt je Revision und Fähigkeit. Prüfprotokolle müssen Messbereiche, Belastung, Ausfall-/Trennverhalten und Qualität der Daten belegen. Keine automatische Hochstufung durch ein vorhandenes Profil oder einen erfolgreichen Softwaretest.

Aktive Integration ist eine separate spätere Freigabe: bevorzugt dokumentierte externe Herstellerschnittstellen unter Erhalt der Originalschutzfunktionen. Gas-/Dieselverbrennung, Zündung, Flammenüberwachung, Übertemperatur, Boiler-Druck-/Temperaturschutz und bei Elektrogeräten Netztrennung/Schutzleiter erfordern gerätespezifische Bewertung. Keine universelle Aktoransteuerung und keine Überbrückung. Der X-Ersatzsteuerungszweig bleibt separat mit eigenem überprüftem Sicherheitskonzept und regulatorischer Freigabe.

## Nächste Schritte

E1800-H1 als ersten durchgängigen Diagnosepfad fertigstellen. Danach je ein konkretes Dieselgerät, ein Boiler und eine Elektroheizung anhand verfügbarer Unterlagen auswählen. Für jedes Gerät Profil, Adapterbedarf und gas-/brennstofffreien beziehungsweise elektrisch geeigneten Prüfstand separat entwickeln. Erst nach überprüften Profilen allgemeine Treiber abstrahieren; keine pauschale Behauptung einer Unterstützung aller Modelle.
