d = 5.7;
dy = 10;
dx = dy*.7559289;
echo(dx);
w = 10;
h = 8;
$fn=20;
difference(){
    cube([3+dx*w,3+dy*h,1],center=true);
    translate([-(dx*(w+1)/2),-(dy*(h+1)/2),0])
    for(i=[1:w]){
        for(j=[1:h]){
            translate([i*dx,j*dy,0.0])cylinder(20,d=d,center=true);
        }
    }
}