#!/bin/bash
#
# make-default.sh
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Thursday January 28, 2021
#
# Distributed under terms of the MIT license.
#

cat << EOF > ~/.local/share/applications/qutebrowser.desktop
[Desktop Entry]
Type=Application
Name=qutebrowser
Exec=/usr/bin/qutebrowser
MimeType=x-scheme-handler/unknown;x-scheme-handler/about;x-scheme-handler/https;x-scheme-handler/http;text/html;
EOF

xdg-settings set default-web-browser qutebrowser.desktop
