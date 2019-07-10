import os
import routes
import importlib

def make_handler(app_handler):
    routes_file = []
    tornado_routes = []
    for root, dires, files in os.walk("handlers/"):
        for filename in files:
            if "routes.py" in filename and ".swp" not in filename:
                routes_file.append(((root + "/" + filename.replace(".py", "")).replace("/", ".")).replace('\\',"."))
            if "handler.py" in filename and ".swp" not in filename:
                tornado_routes.append(((root + "/" + filename.replace(".py", "")).replace("/", ".")).replace('\\',"."))

    route_modules = [importlib.import_module(x) for x in routes_file]
    handler_modules = [importlib.import_module(x) for x in tornado_routes]
    
    tornado_handlers =[(routes.ROUTE, app_handler)]
    for key, value in enumerate(handler_modules):
        print( key, value)
        tornado_handlers.append((route_modules[key].ROUTE, value.Handler))
        
    return tornado_handlers

