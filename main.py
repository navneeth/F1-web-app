from fasthtml.common import *
from monsterui.all import *

from drivers import f1_drivers  # Import the list of F1 drivers from drivers.py


# Choose a theme color (blue, green, red, etc)
hdrs = Theme.blue.headers()

# Create your app with the theme
_app, rt = fast_app(hdrs=hdrs)
app = _app
application = app
handler = app

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

def ex_card3():
    def team_member(name, role, location="Remote"):
        return Card(
            DivLAligned(
                DiceBearAvatar(name, h=24, w=24),
                Div(H3(name), P(role))),
            footer=DivFullySpaced(
                DivHStacked(UkIcon("flag", height=16), P(location)),
                DivHStacked(*(UkIconLink(icon, height=16) for icon in ("car", "flag", "trophy")))))

    team = [
        team_member(driver[0], driver[1], driver[2])
        for driver in f1_drivers
    ]

    return Grid(*team, cols_sm=1, cols_md=1, cols_lg=2, cols_xl=3)


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
			ex_card3(),
			hx_get="/change", style='padding:24px; text-align:center;'
		)
	)
# ============================================================================
# Run the app
# ============================================================================

serve()