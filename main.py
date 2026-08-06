from fasthtml.common import *
from monsterui.all import *

# Choose a theme color (blue, green, red, etc)
hdrs = Theme.blue.headers()

# Create your app with the theme
app, rt = fast_app(hdrs=hdrs)


# Include a CDN link for monsterui (will load styles if available)
MonsterCSS = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/monsterui@latest/dist/monsterui.min.css")

# Simple navbar using basic HTML structure; classes can be picked up by monsterui if present
def Navbar():
	return Div(
		Div('Logo', _class='nav-logo', style='font-weight:700;'),
		Div(
			A('Teams', href='/teams', style='margin:0 12px; color:inherit; text-decoration:none;'),
			A('Drivers', href='/drivers', style='margin:0 12px; color:inherit; text-decoration:none;'),
			A('Calendar', href='/calendar', style='margin:0 12px; color:inherit; text-decoration:none;'),
			A('History', href='/history', style='margin:0 12px; color:inherit; text-decoration:none;'),
			A('About', href='/about', style='margin:0 12px; color:inherit; text-decoration:none;'),
			_class='nav-links',
			style='display:flex; align-items:center;'
		),
		_class='monster-navbar',
		style='display:flex; justify-content:space-between; align-items:center; padding:12px 20px; background:#111; color:#fff;'
	)


def ex_card2_wide():
    def Tags(cats): return DivLAligned(map(Label, cats))

    return Card(
        DivLAligned(
            A(Img(src="https://fansbrands.co.uk/cdn/shop/articles/mclaren_auto_5_91765264-1a0b-4147-bc9f-ea0e6e793451.jpg?v=1759868172&width=1600", style="width:200px"),href="#"),
            Div(cls='space-y-3 uk-width-expand')(
                H4("Explore upcoming F1 Grand prix events (with results)"),
                P("Subscribe to get live uptates and results from all the F1 grand "),
                DivFullySpaced(map(Small, ["McLaren", "20-October-2024"]), cls=TextT.muted),
                DivFullySpaced(
                    Tags(["FastHTML", "HTMX", "Web Apps"]),
                    Button("Read", cls=(ButtonT.primary,'h-6'))))),
        cls=CardT.hover)


@rt('/')
def get():
	# page content: include the monsterui stylesheet link followed by navbar and main content
	return Div(
		MonsterCSS,
		Navbar(),
		Div(
			Img(src='/public/f1-logo.svg', alt='F1 Logo', style='height:64px; display:block; margin:18px auto;'),
			P('F1 Grand Prix Live!'),
			# Embed the F1 card example directly on the homepage
			ex_card2_wide(),
			hx_get="/change", style='padding:24px; text-align:center;'
		)
	)

serve()