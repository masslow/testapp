import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt = urwid.Text("Hello World")
fill = urwid.Filler(txt, 'bottom')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()