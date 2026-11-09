# Diagnose-Skelett

`diagnostics.hpp` ist der hardwarefreie C++17-Kern, `sim.cpp` erzeugt deterministische DEMO-Frames in CSV und JSON. Keine GPIOs, ADCs oder Aktoren werden angesprochen.

ESP32-Portierung: ESP-IDF-Projekt für WROOM-32E nach Frontend-Freigabe ergänzen; Acquisition-Interface von SyntheticSource auf gemessene, kalibrierte Werte umstellen. FreeRTOS-Queues begrenzen, Überlaufzähler und Watchdog ergänzen. CYD-Firmware separat nach Identifikation von Display-/Touch-Controller und Board-Pins. Derzeit ist keine ESP32-Binärdatei und kein CYD-Treiber enthalten.

Format v1: `schema_version,sequence,timestamp_ms,source,channel,value,unit,quality,state`. Demoquelle ausschließlich `synthetic`, Zustand `DEMO`, Qualität `demo`. Messquelle darf später nur bei gültiger Kalibrierung `valid` melden. Keine Interpretation als Flammen-/Sicherheitsstatus.
