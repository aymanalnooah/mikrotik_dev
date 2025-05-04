




/system scheduler   set interval=3h [find where name="LG MAC" ]; 

 /system scheduler set  interval=4h [find where name="remove cookie " ]; 

   /system scheduler  set  interval=5h  [find where name="lease busy remove" ];  


:do {:delay 120; :local testhost "8.8.8.8"; :put "جارِ التحقق من وجود الإنترنت..."; :if ([/ping $testhost count=3] > 0) do={:put "الاتصال بالإنترنت متوفر، جاري التحقق من الملفات..."; :local updateFiles do={:local filename $1; :local url $2; :local files [/file find where name~$filename]; :local success 0; :local failed 0; :if ([:len $files] > 0) do={:put ("تم العثور على " . [:len $files] . " ملف/ملفات باسم " . $filename . " للتحديث."); :foreach i in=$files do={:local fileName [/file get $i name]; :put ("جاري تحديث الملف: " . $fileName); /tool fetch url=$url dst-path=$fileName keep-result=yes; :local newSize [/file get $i size]; :if ($newSize > 0) do={:put ("تم تحديث الملف: " . $fileName); :set success ($success + 1);} else={:put ("فشل تحديث الملف: " . $fileName . " (قد يكون الاتصال فشل)"); :set failed ($failed + 1);}; :delay 1;}; :put ("النتيجة لـ " . $filename . ": نجاح " . $success . " ملف، فشل " . $failed . " ملف.");} else={:put ("لم يتم العثور على أي ملفات باسم " . $filename . ".");};}; $updateFiles "cg.js" "https://raw.githubusercontent.com/aymanalnooah/mikrotik_dev/main/cg.js"; $updateFiles "en.js" "https://raw.githubusercontent.com/aymanalnooah/mikrotik_dev/main/en.js"; :put "تم الانتهاء من محاولة التحديث لجميع الملفات.";} else={:put "لا يوجد اتصال بالإنترنت. سيتم الانتظار 10 دقائق قبل المحاولة مرة أخرى."; :delay 600;};}

