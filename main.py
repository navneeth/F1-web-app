from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get(): return Div(P('F1 Grand Prix Live!'), hx_get="/change")

serve()