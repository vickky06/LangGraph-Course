from typing import Optional, Type, List
from langchain_core.messages import AIMessage
from langchain_core.tools import BaseTool
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from ..llm.interface import LLMInterface
from ..llm.factory import LLMFactory
from .base import AgentInterface

SYSTEM_MESSAGE = """
You are a helpful assistant that can use tools to answer questions.
"""

class AgentNode(AgentInterface):
    """Implementation of an agent node that can use LLM and tools."""
    
    def __init__(self, llm_type: Type[LLMInterface]):
        """Initialize the agent with an LLM implementation.
        
        Args:
            llm_type: Class that implements LLMInterface
        """
        self.llm_manager = LLMFactory.create_llm(llm_type)
        self.tools_list = self.llm_manager.get_tools()
        self.llm = self.llm_manager.get_llm(self.tools_list)
        self.tool_node = ToolNode(self.tools_list)

    def get_tools(self) -> List[BaseTool]:
        """Get list of tools available to the agent."""
        return self.tools_list

    def run_agent_reasoning(self, state: Optional[MessagesState] = None) -> MessagesState:

        """
        Run the agent reasoning node.
        """
        response = self.llm.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]])
        return {"messages": [response]}
      
