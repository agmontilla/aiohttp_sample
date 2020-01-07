from views import handle_get_language, handle_post_language


def setup_routes(app):
    app.router.add_route('GET', '/language', handle_get_language)
    app.router.add_route('POST', '/language', handle_post_language)
