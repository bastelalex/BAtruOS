// Generate placement.scad with placement.py and add its directory via -I.
include <placement.scad>
board = [100, 80];
clearance = 0.5;
wall = 5;
base = 3;
ledge = 2;
holes = []; // verified board-local [x,y] only
pin_d = 2;
part = "all";
$fn = 32;
module nest() {
    difference() {
        cube([board[0]+2*wall, board[1]+2*wall, base+6]);
        translate([wall-clearance,wall-clearance,base])
            cube([board[0]+2*clearance,board[1]+2*clearance,7]);
        translate([wall+ledge,wall+ledge,-1])
            cube([board[0]-2*ledge,board[1]-2*ledge,base+2]);
        for(h=holes) translate([wall+h[0],wall+h[1],-1]) cylinder(d=pin_d+0.3,h=12);
    }
}
module frame() {
    difference() {
        cube([board[0]+2*wall,board[1]+2*wall,3]);
        translate([wall+ledge,wall+ledge,-1]) cube([board[0]-2*ledge,board[1]-2*ledge,5]);
    }
}
module holders() {
    for(i=[0:len(placements)-1]) translate([i*16,0,0]) {
        difference() { cube([12,12,6]); translate([2,2,2]) cube([8,8,5]); }
    }
}
module pins() { for(i=[0:1]) translate([i*10,0,0]) cylinder(d=pin_d,h=10); }
if(part=="all" || part=="nest") nest();
if(part=="all" || part=="frame") translate([board[0]+20,0,0]) frame();
if(part=="all" || part=="holders") translate([0,board[1]+20,0]) holders();
if(part=="all" || part=="pins") translate([0,board[1]+40,0]) pins();
