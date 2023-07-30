

/ip firewall address-list
add address=157.240.227.0/24 comment="What" list=LAN2024
add address=157.240.0.0/16 comment="What" list=facebook_dst
add address=23.90.159.38 list=0TIKTOK comment=free
add address=202.81.112.209 list=0TIKTOK comment=free
add address=71.18.1.229 comment="free fire" list=0TIKTOK
add address=71.18.1.236 comment="free fire" list=0TIKTOK


#remove old

remove [find address=157.240.227.61 list=0TIKTOK]
remove [find address=157.240.227.1 list=0TIKTOK]
remove [find address=34.104.35.84 list=0TIKTOK]
remove [find address=219.93.26.46 list=0TIKTOK]

