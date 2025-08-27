A LangGraph-based AI agent project that demonstrates the implementation of conversational AI agents using LangChain and Google's Generative AI.

# LangGraph Course

A LangGraph-based AI agent project that demonstrates the implementation of conversational AI agents using LangChain and Google's Generative AI.

## Implementing Your Own LangGraph Agent

### 1. Define Your LLM Implementation
Implement the `LLMInterface` to create your own LLM manager:

```python
from src.llm.interface import LLMInterface

class CustomLLMManager(LLMInterface):
    @property
    def model(self) -> str:
        return "your-model-name"

    @property
    def temperature(self) -> float:
        return 0.7

    def get_llm(self, tools=None):
        # Initialize your LLM here
        pass

    def get_tools(self):
        # Return available tools
        pass
```

### 2. Create Custom Tools
Define tools using the `@tool` decorator:

```python
from langchain_core.tools import tool

@tool
def custom_tool(input_data: str) -> str:
    """Tool description for the agent."""
    # Implement tool logic
    return processed_result

# Register in tools/basic_tools.py
def register_tools():
    return [
        custom_tool,
        # other tools...
    ]
```

### 3. Implement Agent Node
Your agent should implement the `AgentInterface`:

```python
from src.agents.base import AgentInterface

class CustomAgent(AgentInterface):
    def __init__(self, llm_type: Type[LLMInterface]):
        self.llm_manager = llm_type()
        # Initialize agent

    def run_agent_reasoning(self, state=None):
        # Implement agent reasoning
        pass

    def get_tools(self):
        # Return agent tools
        pass
```

### 4. Create Graph Flow
Define your graph structure:

```python
from src.graph.flow import create_graph

# Initialize agent
agent = CustomAgent(llm_type=CustomLLMManager)

# Create graph
graph = create_graph(
    run_agent_reasoning=agent.run_agent_reasoning,
    tool_node=agent.tool_node
)

# Use the graph
result = graph.invoke({
    "messages": [
        HumanMessage(content="Your query here")
    ]
})
```

## Project Structure

```
LangGraph-Course/
├── src/
│   ├── agents/      # Agent implementations
│   ├── llm/         # LLM interface and implementations
│   ├── tools/       # Custom tools
│   └── config/      # Configuration management
├── tests/           # Test cases
└── pyproject.toml   # Poetry configuration
```

## Setup

1. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Set up environment variables in `.env`:
```
GOOGLE_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
GOOGLE_MODEL=gemini-1.5-flash
MODEL_TEMPERATURE=0.7
```

## Usage

1. Activate the virtual environment (choose one method):
```bash
# Method 1: Direct activation (recommended)
source $(poetry env info --path)/bin/activate

# Method 2: Using poetry env command
poetry env use python
```

2. Run the project (either method works):
```bash
# If environment is activated:
python -m src.main

# Or using poetry run (works without activation):
poetry run start
```

## Development

- Format code: `poetry run black .`
- Run tests: `poetry run pytest`
- Add dependency: `poetry add package-name`
- Add dev dependency: `poetry add --group dev package-name`

## Graph Flow Explanation

The LangGraph agent uses a state machine with the following nodes:

1. `AGENT_REASON`: Main reasoning node
   - Receives user input or previous state
   - Decides next action
   - Can transition to `ACT` or `END`

2. `ACT`: Tool execution node
   - Executes selected tool
   - Always returns to `AGENT_REASON`

3. `END`: Terminal node
   - Ends the conversation
   - Returns final state

Flow:
```
[Start] -> [AGENT_REASON] -> (decides) -> [ACT] -> [AGENT_REASON]
                         -> (decides) -> [END]
```

### State Management

The state object has this structure:
```python
{
    "messages": [
        SystemMessage(content="..."),
        HumanMessage(content="..."),
        AIMessage(content="...", tool_calls=[...]),
        ToolMessage(content="...")
    ]
}
```

## Best Practices

1. **Interface Implementation**
   - Always implement provided interfaces
   - Use proper type hints
   - Document public methods

2. **Tool Development**
   - Keep tools atomic and focused
   - Provide clear descriptions
   - Handle errors gracefully

3. **State Management**
   - Don't modify state directly
   - Use immutable patterns
   - Validate state transitions

4. **Testing**
   - Test each component independently
   - Verify tool behaviors
   - Test state transitions

## License

MIT
