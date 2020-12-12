#!/usr/bin/env python


def toggleMargins(qtile):
    if qtile.current_layout.margin == 0:
        qtile.current_layout.margin = 12
    else:
        qtile.current_layout.margin = 0

def incMargins(qtile):
    qtile.current_layout.margin = qtile.current_layout.margin + 6

def decMargins(qtile):
    qtile.current_layout.margin = qtile.current_layout.margin - 6
