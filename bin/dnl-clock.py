#!/usr/bin/env python
#

# gi.require_version('Gtk', '3.0')
from gi.repository import AppIndicator3 as app

# from gi.repository import Gtk as gtk, AppIndicator3 as appindicator
def main():
  indicator = app.Indicator.new("customtray", "semi-starred-symbolic", app.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(app.IndicatorStatus.ACTIVE)

main()
