from functools import wraps

from .db import DataStorage


def db_init_with_credentials(view_func):
    """
    Decorator for views that initializes DataStorage class with 
    organization_id and plugin_id dynamically
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Capture org_id param, add it to request.META and exclude it from function arguments
        if kwargs.get("org_id", None):
            request.META["ORG_ID"] = kwargs["org_id"]
            del kwargs["org_id"]

        DB = DataStorage(request)
        view_func.__globals__.update({"DB": DB})
        view = view_func(request, *args, **kwargs)
        return view
    return _wrapped_view
