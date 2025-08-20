# LLM (Language Model)

This directory handles language model implementations and interfaces.

## Purpose
- Define LLM interfaces
- Implement different LLM providers (Google, OpenAI, etc.)
- Handle LLM configuration and state

## Contents
- `interface.py`: Base interface for LLMs (`LLMInterface`)
- `factory.py`: Factory for creating LLM instances
- `implementations.py`: Concrete LLM implementations

## When to Add Code Here
Add code here when you need to:
1. Add support for a new LLM provider
2. Modify LLM behavior or configuration
3. Implement new LLM capabilities
4. Add custom LLM wrappers

## Example
```python
class CustomLLM(LLMInterface):
    @property
    def model(self) -> str:
        return "custom-model"
        
    @property
    def temperature(self) -> float:
        return 0.7
        
    def get_llm(self, tools=None):
        # Implement LLM initialization
        pass
```
