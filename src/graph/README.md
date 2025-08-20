# Graph

This directory manages the workflow and graph structure of the agent system.

## Purpose
- Define the flow of agent operations
- Manage state transitions
- Configure graph nodes and edges
- Handle workflow visualization

## Contents
- `flow.py`: Graph structure and workflow definitions
- `constants.py`: Graph-related constants
- `interfaces.py`: Graph component interfaces

## When to Add Code Here
Add code here when you need to:
1. Modify the agent workflow
2. Add new states or transitions
3. Change graph behavior
4. Add visualization options

## Example
```python
def create_agent_graph() -> StateGraph:
    flow = StateGraph(MessagesState)
    # Add nodes and edges
    return flow.compile()
```

## Guidelines
- Keep state transitions clear
- Document graph structure
- Use constants for node names
- Include visualization helpers
