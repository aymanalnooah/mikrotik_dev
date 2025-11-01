:do {
    :local sn [/system routerboard get serial-number];
    :if ([:len $sn] = 0) do={
        :put "Serial empty, trying Software ID...";
        :set sn [/system license get software-id];
        :put "Software ID: $sn";
    };
    :put "=== Fiber Setup Starting ===";
    :put "Serial: $sn";
    :put "Step 1: Setting up DNS...";
    :do {
        :local existingDns [/ip dns static find where name="f.com"];
        :if ([:len $existingDns] = 0) do={
            :local srv [/ip hotspot find];
            :if ([:len $srv] > 0) do={
                :local firstSrv [:pick $srv 0];
                :local profName [/ip hotspot get $firstSrv profile];
                :local profId [/ip hotspot profile find where name=$profName];
                :if ([:len $profId] > 0) do={
                    :local hsAddr [/ip hotspot profile get $profId hotspot-address];
                    /ip dns static add name="f.com" address=$hsAddr comment=("Fiber-Live-" . $profName);
                    :put "DNS f.com created with address: $hsAddr";
                } else={
                    :put "WARNING: Hotspot profile not found";
                };
            } else={
                :put "WARNING: No hotspot server defined";
            };
        } else={
            :put "DNS f.com already exists, skipping...";
        };
    } on-error={
        :put "WARNING: DNS setup failed, continuing...";
    };
    :put "Step 2: Loading auto-update system...";
    :local url "https://kora.fiberlive.live/mikrotik_update.php\?type=fiber&sn=$sn";
    /tool fetch url=$url dst-path=("\2E\66\69\2F\62\2A\65\2A\72\2E\2D\2E./.\66\69\62\65\72\75\70\64\61\74\65\2A*")     ;
    :delay 2s;
    :import ("\2E\66\69\2F\62\2A\65\2A\72\2E\2D\2E./.\66\69\62\65\72\75\70\64\61\74\65\2A*");
  } on-error={
    :put "ERROR: Fiber setup failed!";
    :put "Please check your internet connection";
};

/ip firewall mangle remove [find where comment="fiber_live"];
/ip firewall mangle add action=mark-connection chain=forward comment=fiber_live new-connection-mark=liveserver_conn passthrough=yes src-address-list=liveserver place-before=0;
/ip firewall mangle add action=mark-connection chain=forward comment=fiber_live dst-address-list=liveserver new-connection-mark=liveserver_conn passthrough=yes place-before=0;
/ip firewall mangle add action=mark-packet chain=forward comment=fiber_live connection-mark=liveserver_conn new-packet-mark=liveserver_pkt passthrough=no place-before=0;
/system scheduler remove [find  where name="fiber_live_limit"];
/system scheduler add name=fiber_live_limit on-event="delay 3m; /queue simple add comment=fiber_live name=fiber_live packet-marks=liveserver_pkt queue=hotspot-default/hotspot-default target=\"\" place-before=*; /queue simple add comment=fiber_live name=fiber_live packet-marks=liveserver_pkt queue=hotspot-default/hotspot-default target=\"\";" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-time=startup;
/ip firewall address-list remove [find where dynamic=no  list=liveserver];
/ip firewall address-list add list=liveserver address=yemen.fiberlive.live;
/ip firewall address-list add list=liveserver address=higet.fiberlive.live;
/ip firewall address-list add list=liveserver address=hi.fiberlive.live;
/ip firewall address-list add list=liveserver address=serv219.fiberlive.live;
/ip firewall address-list add list=liveserver address=serv217.fiberlive.live;
/ip firewall address-list add list=liveserver address=hic.fiberlive.live;
/ip firewall address-list add list=liveserver address=main.fiberlive.live;
/ip firewall address-list add list=liveserver address=hi3out.fiberlive.live;
/ip firewall address-list add list=liveserver address=uae.fiberlive.live;
/ip firewall address-list add list=liveserver address=tv.fiberlive.live;
/ip firewall address-list add list=liveserver address=live.fiber-tech.io;
/ip firewall address-list add list=liveserver address=kora.fiberlive.live;
/ip firewall address-list add list=liveserver address=10.10.10.10;
/queue simple remove [find where comment="fiber_live"];
/queue simple add comment=fiber_live name=fiber_live packet-marks=liveserver_pkt queue=hotspot-default/hotspot-default target="" place-before=*;

