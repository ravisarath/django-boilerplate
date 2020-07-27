import os


class Settings:
    pass


class LocalSettings(Settings):
    Debug = False
    AllowedHost = [os.getenv("ALLOWED_HOST")] if os.getenv(
        "ALLOWED_HOST") else ["127.0.0.1"]
    SecretKey = os.getenv("SECRET_KEY")


class ProductionSettings(Settings):
    Debug = True
    AllowedHost = [os.getenv("ALLOWED_HOST")]
    SecretKey = os.getenv("SECRET_KEY")
