# Agents

This directory contains agent-related implementations and interfaces.

## Purpose
- Define agent behaviors and interfaces
- Implement different types of agents
- Handle agent state and reasoning

## Contents
- `base.py`: Base interface for agents (`AgentInterface`)
- `nodes.py`: Concrete agent implementations (`AgentNode`)

## When to Add Code Here
Add code here when you need to:
1. Create a new type of agent
2. Modify agent behavior
3. Add new agent capabilities
4. Implement agent state management

## Example
```python
class CustomAgent(AgentInterface):
    def get_tools(self) -> List[BaseTool]:
        # Return available tools
        pass
        
    def run_agent_reasoning(self, state: Optional[MessagesState] = None) -> MessagesState:
        # Implement agent reasoning
        pass
```
