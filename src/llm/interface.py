from abc import ABC, abstractmethod
from typing import Any, List, Optional
from langchain_core.tools import BaseTool

class LLMInterface(ABC):
    """Abstract base class for LLM implementations."""
    
    @property
    @abstractmethod
    def model(self) -> str:
        """Get the model name."""
        pass

    @property
    @abstractmethod
    def temperature(self) -> float:
        """Get the temperature setting."""
        pass

    @abstractmethod
    def get_llm(self, tools: Optional[List[BaseTool]] = None) -> Any:
        """Get LLM instance with optional tools."""
        pass

    @abstractmethod
    def get_tools(self) -> List[BaseTool]:
        """Get list of available tools."""
        pass
