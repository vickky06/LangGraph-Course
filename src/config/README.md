# Configuration

This directory manages project configuration and settings.

## Purpose
- Handle environment variables
- Manage project settings
- Provide configuration interfaces

## Contents
- `settings.py`: Core configuration implementation
- Environment variable handling
- Configuration enums and types

## When to Add Code Here
Add code here when you need to:
1. Add new configuration options
2. Modify configuration behavior
3. Add new environment variables
4. Implement configuration validation

## Example
```python
class NewConfigKey(Enum):
    NEW_SETTING = "NEW_SETTING"

def validate_config():
    """Validate configuration values."""
    required_keys = [
        ConfigKey.GOOGLE_API_KEY,
        ConfigKey.MODEL_TEMPERATURE
    ]
    # Implement validation
```

## Guidelines
- Use strong typing
- Validate configurations
- Document all settings
- Use environment variables for sensitive data
