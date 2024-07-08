from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    FARM_MINING_ERA: bool = True
    TAPS: bool = True
    TAPS_AMOUNT: list[int] = [100, 1000]
    CLAIM_SQUAD_REWARD: bool = True
    CLAIM_TASKS: bool = True
    REF_ID: str = ''

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
