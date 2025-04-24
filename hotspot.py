/ip firewall address-list ;




 enable   [ find where  address=216.239.38.0/24 ] ;  
 disable   [ find where  address=142.251.0.0/16 ] ;  


add address=57.144.149.0/24 comment=whats list=Whats-face ; 
add address=216.239.35.0/24 comment=whats list=Whats-face ; 
add address=31.13.88.0/24 comment=whats list=Whats-face ; 
add address=time.android.com comment=whats list=Whats-face ; 
add address=g.whatsapp.net comment=whats list=Whats-face ; 
add address=g-fallback.whatsapp.net comment=whats list=Whats-face ; 
add address=android.googleapis.com comment=whats list=Whats-face ; 

