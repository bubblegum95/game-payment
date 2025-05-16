from decouple import config

TORTOISE_ORM = {
    "connections": {"default": config("DB_URL")},
    "apps": {
        "models": {
            "models": ["app.models.user_model", "app.models.pay_model", "aerich.models"],
            "default_connection": "default",
        },
    },
}
