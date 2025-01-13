




/ip hotspot walled-garden
add dst-host=*tvquran.com*


add dst-host=*quran.tv*


/ip firewall address-list

add address=quran.tv list=hotspot.alnooah
add address=tvquran.com list=hotspot.alnooah
add address=quran.tv list=tvquran.com
add address=tvquran.com list=tvquran.com


