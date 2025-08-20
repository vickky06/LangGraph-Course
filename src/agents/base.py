from abc import ABC, abstractmethod
from typing import List, Optional
from langchain_core.tools import BaseTool
from langgraph.graph import MessagesState

class AgentInterface(ABC):
    """Abstract base class for agent implementations."""
    
    @abstractmethod
    def get_tools(self) -> List[BaseTool]:
        """Get list of tools available to the agent."""
        pass
    
    @abstractmethod
    def run_agent_reasoning(self, state: Optional[MessagesState] = None) -> MessagesState:
        """Run the agent's reasoning process.
        
        Args:
            state: Current message state
            
        Returns:
            Updated message state
        """
        pass
