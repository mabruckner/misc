module gear(r,nt,td,tp){
    inc = 360/nt;
    l = r-td/2;
    h = r+td/2;
    plist = [
    for(i=[0:nt-1])
        for(j=[[inc*i,h],[inc*(i+.5-tp),h],[inc*(i+.5),l],[inc*(i+1-tp),l]])
            [j[1]*cos(j[0]),j[1]*sin(j[0])]];
    echo(plist);
    polygon(plist);
}
gear(10,100,.4,.2);
translate([10,0.0])gear(2,20,.4,.2);
//circle(r=10);