fastboot erase la_cache
fastboot flash la_cache cache.img
fastboot erase la_persist
fastboot flash la_persist persist.img
fastboot erase la_userdata
fastboot flash la_userdata userdata.img
fastboot erase la_vendor
fastboot flash la_vendor vendor.img
fastboot erase la_system
fastboot flash la_system system.img