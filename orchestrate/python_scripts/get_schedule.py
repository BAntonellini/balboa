import os


def get_schedule(default_input):
    # Return None if development environment, cron schedule if prod.
    env_slug = os.environ.get("DATACOVES__ENVIRONMENT_SLUG", "").lower()
    if env_slug == "dev123":
        return None
    else:
        return default_input