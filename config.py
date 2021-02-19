# --------------------------------------------------------------------
# config.py
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Monday June 15, 2020
#
# Distributed under terms of the MIT license.
# --------------------------------------------------------------------

# type: ignore
from qutebrowser.config.configfiles import ConfigAPI # noqa: F401
from qutebrowser.config.config import ConfigContainer # noqa: F401
config: ConfigAPI = config # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c # noqa: F821 pylint: disable=E0602,C0103
from pathlib import Path
import re
import json

# -------------------------------------------------------------------
def load_font_config():
    font_config = Path.home() / ".font" / "config.json"

    with open(font_config, "r") as infile:
        return json.load(infile)

# -------------------------------------------------------------------
def load_base16():
    xdefaults_file = Path.home() / ".Xdefaults"

    base16 = {}
    with open(xdefaults_file, "r") as infile:
        for line in infile.readlines():
            match = re.match(r"#define (base.*) (#.*)$", line.strip())
            if match:
                base16[match.group(1)] = match.group(2)
    return base16

# -------------------------------------------------------------------
BASE16 = load_base16()
FONT = load_font_config()

# -------------------------------------------------------------------
# Config settings
# -------------------------------------------------------------------
#config.load_autoconfig(False) # Don't load autoconfig.yaml.
config.load_autoconfig()
c.completion.cmd_history_max_items = -1
c.tabs.last_close = "close"

# -------------------------------------------------------------------
# Content Settings
# -------------------------------------------------------------------
c.content.autoplay = False
c.content.blocking.whitelist = []
c.content.canvas_reading = False
c.content.fullscreen.overlay_timeout = 0
c.content.fullscreen.window = True
c.content.mute = False
c.content.pdfjs = True

c.downloads.position = "bottom"
c.editor.command = ["termite", "-e", "vim {file}"]

c.input.insert_mode.leave_on_load = True

# -------------------------------------------------------------------
# Appearance settings
# -------------------------------------------------------------------
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.bg = BASE16["base00"]
c.colors.tabs.bar.bg = BASE16["base00"]
c.colors.tabs.even.bg = BASE16["base00"]
c.colors.tabs.odd.bg = BASE16["base00"]
c.colors.tabs.selected.even.bg = BASE16["base01"]
c.colors.tabs.selected.odd.bg = BASE16["base01"]
c.colors.statusbar.normal.bg = BASE16["base00"]
c.colors.statusbar.command.bg = BASE16["base00"]
c.colors.statusbar.insert.bg = BASE16["base01"]
c.colors.statusbar.insert.fg = BASE16["base05"]
c.fonts.default_family = FONT["font"]
c.fonts.default_size = "%dpt" % (FONT["size"] - 8)
c.messages.timeout = 1000

# -------------------------------------------------------------------
# URL settings
# -------------------------------------------------------------------
c.url.searchengines["DEFAULT"] = "https://google.com/search?q={}"
c.url.searchengines["aw"] = "https://wiki.archlinux.org/?search={}"
c.url.start_pages = ["about:blank"]
c.url.default_page = "about:blank"

# -------------------------------------------------------------------
# Key bindings
# -------------------------------------------------------------------
config.bind("J", "tab-prev")
config.bind("K", "tab-next")
config.bind(";i", "hint images userscript qute-open-url")
config.bind(";s", "spawn --userscript qute-search-selection")
config.bind("A", "tab-mute")
