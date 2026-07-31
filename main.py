from fasthtml.common import *

app,rt = fast_app()

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


@rt('/')
def get():
	# page content: include the monsterui stylesheet link followed by navbar and main content
	return Div(
		MonsterCSS,
		Navbar(),
		Div(P('F1 Grand Prix Live!'), hx_get="/change", style='padding:24px;')
	)

serve()