from typing import Dict, Any, List, Optional
from langchain_core.tools import tool, BaseTool
from langchain_tavily import TavilySearch
from typing import Union
from ..config.settings import get_config, ConfigKey

@tool
def tripple_number(x: Union[int, float]) -> float:
    """Triple a number.
    
    Args:
        x (float): Number to triple
        
    Returns:
        float: Tripled value
    """
    print(f"Tripling {x}")
    return x * 3

def register_tools() -> List[BaseTool]:
    """Register all available tools.
    
    Returns:
        List[BaseTool]: List of available tools
    """
    # Initialize Tavily search with API key
    tavily_api_key = get_config(ConfigKey.TAVILY_API_KEY)
    search_tool = TavilySearch(max_results=1,topic="general",api_key=tavily_api_key)
    
    available_tools = [
        tripple_number,
        search_tool,  # Add Tavily search
        # Add more tools here as needed
    ]
    return available_tools

def get_tool_by_name(tool_name: str) -> Optional[BaseTool]:
    """Get a specific tool by name.
    
    Args:
        tool_name: Name of the tool to retrieve
        
    Returns:
        Optional[BaseTool]: The requested tool or None if not found
    """
    tools_dict = {tool.name: tool for tool in register_tools()}
    return tools_dict.get(tool_name)
