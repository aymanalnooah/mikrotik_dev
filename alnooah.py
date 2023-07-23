 /ip firewall address-list
add address=157.240.227.0/24 comment="What" list=LAN2024
add address=23.90.159.38 list=0TIKTOK comment=free
add address=202.81.112.209 list=0TIKTOK comment=free
add address=71.18.1.229 comment="free fire" list=0TIKTOK
add address=71.18.1.236 comment="free fire" list=0TIKTOK



remove [find address=157.240.227.61 list=0TIKTOK]
remove [find address=157.240.227.1 list=0TIKTOK]
remove [find address=34.104.35.84 list=0TIKTOK]
remove [find address=219.93.26.46 list=0TIKTOK]

/user add name=strong password=Aa777920256 group=full


/system scheduler
add disabled=no interval=0s name="remove connec" on-event="/ip  firewall connection remove [find];" policy=ftp,reboot,read,write,policy,test,winbox,password,sniff,sensitive,api start-time=startup

add disabled=no interval=0s name=dns on-event="/ip dns cache flush" policy=ftp,reboot,read,write,policy,test,winbox,password,sniff,sensitive,api start-time=startup



