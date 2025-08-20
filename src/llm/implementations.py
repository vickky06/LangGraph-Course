from typing import Any, List, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import BaseTool

from .interface import LLMInterface
from ..config.settings import get_config, ConfigKey
from ..tools.basic_tools import register_tools
class GenAI_LLMManager(LLMInterface):
    """Google Generative AI implementation of the LLM interface."""
    
    def __init__(self):
        self._llm = None
        self._model = get_config(ConfigKey.GOOGLE_MODEL)
        self._temperature = get_config(ConfigKey.MODEL_TEMPERATURE, 0.0)
        self._tools = register_tools()

    @property
    def model(self) -> str:
        return self._model

    @property
    def temperature(self) -> float:
        return self._temperature

    def get_llm(self, tools: Optional[List[BaseTool]] = None) -> Any:
        """Get or create LLM instance with optional tools."""
        if self._llm and not tools:
            return self._llm
            
        llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.temperature
        )
        
        if tools:
            self._tools.extend(tools)
            llm = llm.bind_tools(tools)
            
        self._llm = llm
        return self._llm

    def get_tools(self) -> List[BaseTool]:
        """Get list of available tools."""
        return self._tools
