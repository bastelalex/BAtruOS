# Parametrischer Lötassistent

OpenSCAD-Entwurf: PCB-Nest mit Randauflage, wechselbarem Halter, umkehrbarem Klemmrahmen und zwei separat platzierbaren Zentrierstiften. Nur Einlege-/Montagehilfe, keine thermisch validierte Lötvorrichtung. Material, Temperatur, Bauteilfreiheit und Klemmkraft vor Nutzung prüfen. Rahmen und Halter sind im Drucklayout neben dem Nest angeordnet; nach Druck montieren.

Placement-Vertrag v1: CSV `reference,x_mm,y_mm,rotation_deg,side`; Dezimalpunkt, mm, Ursprung links unten im verifizierten Platinenumriss, +X rechts/+Y oben, Rotation gegen Uhrzeigersinn von oben. Beispiel unterstützt nur Oberseite `top`. KiCad-Export vor Import in diesen Ursprung und Winkelkonvention umrechnen. Fehlende, doppelte, nicht endliche und außerhalb liegende Werte werden abgelehnt. Der Import erzeugt Halter-Anker, keine automatisch passenden Bauteilkonturen; Bauteilhöhe, Körpermaße und Freistellung müssen später aus freigegebenen Footprints ergänzt werden.

`assistant.scad`: board=[100,80] ist nur Entwurfsmaß; Lochpositionen sind bewusst nicht vorgegeben. Zentrierung erst mit gemessenen Löchern (`holes`) aktivieren. Export aller Teile als gemeinsames STL oder über `part` einzeln (`nest`, `frame`, `holders`, `pins`). QR-Anleitung siehe assembly.
