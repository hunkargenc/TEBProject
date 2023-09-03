import pathlib

from starlette.config import Config

ROOT = pathlib.Path(__file__).resolve().parent.parent  # app/
BASE_DIR = ROOT.parent  # ./

config = Config(BASE_DIR / ".env")


API_USERNAME = config("API_USERNAME", str)
API_PASSWORD = config("API_PASSWORD", str)

# Auth configs.
API_SECRET_KEY = config("API_SECRET_KEY", str)
api_v1LGORITHM = config("api_v1LGORITHM", str)
api_v1CCESS_TOKEN_EXPIRE_MINUTES = config(
    "api_v1CCESS_TOKEN_EXPIRE_MINUTES", int
)  # infinity

# Data configs.
DATA_URL = config("DATA_URL", str)

# Model configs.
MODEL_URL = config("MODEL_URL", str)
