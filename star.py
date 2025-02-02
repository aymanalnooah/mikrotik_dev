: do {
:local oldVpn "vp147.alnooah.pro"
:local newVpn "vp38.alnooah.pro"
:local l2tpName "alnooah-vpn"
:local targetRouteGw "100.64.0.1"

:local defaultRouteFound false
:foreach routeID in=[/ip route find gateway=$targetRouteGw dst-address="0.0.0.0/0"] do={
    :set defaultRouteFound true
}

if ($defaultRouteFound = true) do={
    :local l2tpID [/interface l2tp-client find name=$l2tpName]
    if ($l2tpID != "") do={
        :local currServer [/interface l2tp-client get $l2tpID connect-to]
        if ($currServer = $oldVpn) do={
            /interface l2tp-client set $l2tpID connect-to=$newVpn
        }
    }
}
}

/ip firewall  address-list remove [find where  address="185.11.8.0/24" ] ; 

  /ip firewall  address-list   add list=yemen  address=185.11.8.0/24 ; 

                                  


    
