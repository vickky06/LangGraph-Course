from typing import Type
from .interface import LLMInterface

class LLMFactory:
    """Factory class for creating LLM instances."""
    
    @staticmethod
    def create_llm(llm_type: Type[LLMInterface]) -> LLMInterface:
        """Create an instance of the specified LLM type.
        
        Args:
            llm_type: Class that implements LLMInterface
            
        Returns:
            LLMInterface: Instance of the specified LLM type
            
        Raises:
            ValueError: If llm_type doesn't implement LLMInterface
        """
        if not issubclass(llm_type, LLMInterface):
            raise ValueError(f"{llm_type.__name__} must implement LLMInterface")
        return llm_type()
