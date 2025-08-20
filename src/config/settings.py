from dotenv import load_dotenv
import os
from typing import Any, Optional
from enum import Enum
from dataclasses import dataclass

@dataclass
class Config:
    """Configuration class for storing environment variables."""
    GOOGLE_API_KEY: Optional[str] = None
    TAVILY_API_KEY: Optional[str] = None
    LANGCHAIN_ENDPOINT: Optional[str] = None
    LANGCHAIN_PROJECT: Optional[str] = None
    GOOGLE_MODEL: str = "gemini-1.5-flash"
    MODEL_TEMPERATURE: float = 0.7

class ConfigKey(Enum):
    """Enum for configuration keys."""
    GOOGLE_API_KEY = "GOOGLE_API_KEY"
    TAVILY_API_KEY = "TAVILY_API_KEY"
    LANGCHAIN_ENDPOINT = "LANGCHAIN_ENDPOINT"
    LANGCHAIN_PROJECT = "LANGCHAIN_PROJECT"
    GOOGLE_MODEL = "GOOGLE_MODEL"
    MODEL_TEMPERATURE = "MODEL_TEMPERATURE"

_config_instance: Optional[Config] = None

def load_config() -> Config:
    """
    Load configuration from environment variables.
    Returns:
        Config: An instance of Config with loaded values.
    """
    global _config_instance
    if _config_instance is None:
        load_dotenv()
        _config_instance = Config(
            GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY"),
            TAVILY_API_KEY=os.getenv("TAVILY_API_KEY"),
            LANGCHAIN_ENDPOINT=os.getenv("LANGCHAIN_ENDPOINT"),
            LANGCHAIN_PROJECT=os.getenv("LANGCHAIN_PROJECT"),
            GOOGLE_MODEL=os.getenv("GOOGLE_MODEL", "gemini-1.5-flash"),
            MODEL_TEMPERATURE=float(os.getenv("MODEL_TEMPERATURE", "0.7"))
        )
    return _config_instance

def get_config(key: ConfigKey, default: Any = None) -> Any:
    """
    Get a specific configuration value.
    Args:
        key (ConfigKey): The key of the configuration value to retrieve.
        default (Any): The default value to return if the key is not found.
    Returns:
        Any: The value of the specified configuration key.
    """
    config = load_config()
    value = getattr(config, key.value, default)
    return value if value is not None else default
