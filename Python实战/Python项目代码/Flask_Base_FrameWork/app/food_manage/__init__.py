def init_app(app):
    from . import (
        query,
        manage,
    )
    for food_mgmt in [query, manage]:
        blueprint = food_mgmt.blueprint
        app.register_blueprint(blueprint)
