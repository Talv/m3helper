#!/usr/bin/bash

pyuic5 m3helper/ui/main.ui >m3helper/ui/main.py
pyuic5 m3helper/ui/config.ui >m3helper/ui/config.py
pyuic5 m3helper/ui/about.ui >m3helper/ui/about.py
pyrcc5 m3helper/ui/rc.qrc >m3helper/ui/rc_rc.py
sed -i 's/^import rc_rc$/from \.rc_rc import \*/g' m3helper/ui/main.py